pipeline {
    agent any

    parameters {
        choice(name: 'BROWSER', choices: ['chrome', 'firefox', 'edge'], description: 'Браузер для тестов')
        string(name: 'BASE_URL', defaultValue: 'http://prestashop:80/', description: 'URL тестируемого приложения')
        booleanParam(name: 'HEADLESS', defaultValue: true, description: 'Запуск в headless-режиме')
        string(name: 'LOG_LEVEL', defaultValue: 'INFO', description: 'Уровень логирования')
    }

    options {
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 60, unit: 'MINUTES')
        disableConcurrentBuilds()
    }

    environment {
        COMPOSE_DIR     = "${WORKSPACE}\\docker_selenoid"
        COMPOSE_FILE    = "${WORKSPACE}\\docker_selenoid\\docker-compose.yaml"
        COMPOSE_PROJECT = "otus_qa_${BUILD_NUMBER}"
    }

    stages {

        stage('Prepare networks') {
            steps {
                bat '''
                    docker network inspect selenoid1 >NUL 2>&1 || docker network create selenoid1
                    docker network inspect selenoid2 >NUL 2>&1 || docker network create selenoid2
                '''
            }
        }
        stage('Build test image') {
            steps {
                bat """
                    cd /d "${COMPOSE_DIR}"
                    docker compose -p ${COMPOSE_PROJECT} -f "${COMPOSE_FILE}" build tests
                """
            }
        }

        stage('Start infrastructure') {
            steps {
                bat """
                    cd /d "${COMPOSE_DIR}"
                    docker compose -p ${COMPOSE_PROJECT} -f "${COMPOSE_FILE}" up -d selenoid1 selenoid2 ggr ggr_ui selenoid_ui nginx db prestashop
                """
            }
        }

        stage('Wait for PrestaShop healthy') {
            steps {
                powershell '''
                    $ok = $false
                    for ($i=1; $i -le 60; $i++) {
                        $status = docker inspect -f "{{.State.Health.Status}}" prestashop 2>$null
                        Write-Host "[$i/60] prestashop health: $status"
                        if ($status -eq "healthy") { $ok = $true; break }
                        Start-Sleep -Seconds 10
                    }
                    if (-not $ok) {
                        docker logs prestashop --tail 200
                        exit 1
                    }
                '''
            }
        }

        stage('Remove install folders (postinstall)') {
            steps {
                bat """
                    cd /d "${COMPOSE_DIR}"
                    docker compose -p ${COMPOSE_PROJECT} -f "${COMPOSE_FILE}" up -d prestashop_postinstall
                    docker wait prestashop_postinstall
                    docker logs prestashop_postinstall
                """
            }
        }
        stage('Run tests') {
            steps {
                bat """
                    if not exist logs mkdir logs
                    if not exist screenshot mkdir screenshot
                    if not exist reports mkdir reports
                    if not exist allure-results mkdir allure-results
                """

                bat """
                    cd /d "${COMPOSE_DIR}"
                    docker compose -p ${COMPOSE_PROJECT} ^
                        -f "${COMPOSE_FILE}" ^
                    run --rm ^
                        -e BROWSER=${params.BROWSER} ^
                    tests ^
                    pytest test_file ^
                        --browser=${params.BROWSER} ^
                        --url=${params.BASE_URL} ^
                        ${params.HEADLESS ? '--headless' : ''} ^
                        --log_level=${params.LOG_LEVEL} ^
                        --junitxml=reports/junit.xml ^
                        --alluredir=allure-results
                """
            }
        }
    }
post {
    always {
        junit allowEmptyResults: true, testResults: 'reports/*.xml'

        allure includeProperties: false,
               jdk: '',
               results: [[path: 'allure-results']]

        archiveArtifacts artifacts: 'logs/**/*.log, screenshot/**/*.png, reports/**/*.xml, allure-results/**/*', allowEmptyArchive: true

        bat """
            cd /d "${COMPOSE_DIR}"
            docker compose -p ${COMPOSE_PROJECT} -f "${COMPOSE_FILE}" down -v --remove-orphans
        """
        }
    }
}
