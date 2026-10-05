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
        COMPOSE_DIR      = "${WORKSPACE}"
        COMPOSE_FILE     = "${WORKSPACE}/docker-compose.yaml"
        COMPOSE_PROJECT  = "otus_qa_${BUILD_NUMBER}"
        ARTIFACTS_DIR    = "artifacts"
    }

    stages {

        stage('Prepare networks') {
            steps {
                sh '''
                    docker network inspect selenoid1 >/dev/null 2>&1 || docker network create selenoid1
                    docker network inspect selenoid2 >/dev/null 2>&1 || docker network create selenoid2
                '''
            }
        }

        stage('Build test image') {
            steps {
                sh """
                    cd ${COMPOSE_DIR}
                    docker compose -p ${COMPOSE_PROJECT} -f ${COMPOSE_FILE} build tests
                """
            }
        }

        stage('Start infrastructure') {
            steps {
                sh """
                    cd ${COMPOSE_DIR}
                    docker compose -p ${COMPOSE_PROJECT} -f ${COMPOSE_FILE} up -d \\
                        selenoid1 selenoid2 ggr ggr_ui selenoid_ui nginx db prestashop
                """
            }
        }

        stage('Wait for PrestaShop healthy') {
            steps {
                sh """
                    set -e
                    echo "Ожидание healthy-статуса prestashop..."
                    for i in \$(seq 1 60); do
                        STATUS=\$(docker inspect -f '{{.State.Health.Status}}' prestashop 2>/dev/null || echo "unknown")
                        echo "[\$i/60] prestashop health: \$STATUS"
                        if [ "\$STATUS" = "healthy" ]; then
                            echo "prestashop healthy!"
                            exit 0
                        fi
                        sleep 10
                    done
                    echo "prestashop не стал healthy за отведённое время"
                    docker logs prestashop --tail 200 || true
                    exit 1
                """
            }
        }

        stage('Remove install folders (postinstall)') {
            steps {
                sh """
                    cd ${COMPOSE_DIR}
                    docker compose -p ${COMPOSE_PROJECT} -f ${COMPOSE_FILE} up -d prestashop_postinstall
                    docker wait prestashop_postinstall || true
                    docker logs prestashop_postinstall || true
                """
            }
        }

        stage('Run tests') {
            steps {
                sh 'mkdir -p logs screenshot reports'
                sh """
                    cd ${COMPOSE_DIR}
                    docker compose -p ${COMPOSE_PROJECT} -f ${COMPOSE_FILE} run --rm \\
                        -e BROWSER=${params.BROWSER} \\
                        tests \\
                        pytest \\
                            --browser=${params.BROWSER} \\
                            --url=${params.BASE_URL} \\
                            ${params.HEADLESS ? '--headless' : ''} \\
                            --log_level=${params.LOG_LEVEL} \\
                            --junitxml=reports/junit.xml
                """
            }
        }
    }

    post {
        always {
            script {
                sh '''
                    CID=$(docker ps -a --filter "name=${COMPOSE_PROJECT}_tests" --format "{{.ID}}" | head -n1 || true)
                    if [ -n "$CID" ]; then
                        docker cp "$CID":/page_object_test/logs ./logs || true
                        docker cp "$CID":/page_object_test/screenshot ./screenshot || true
                        docker cp "$CID":/page_object_test/reports ./reports || true
                    fi
                '''
            }

            junit allowEmptyResults: true, testResults: 'reports/*.xml'
            archiveArtifacts artifacts: 'logs/**/*.log, screenshot/**/*.png, reports/**/*.xml', allowEmptyArchive: true

            sh """
                cd ${COMPOSE_DIR}
                docker compose -p ${COMPOSE_PROJECT} -f ${COMPOSE_FILE} down -v --remove-orphans || true
            """
        }
        success {
            echo "Тесты успешно пройдены."
        }
        failure {
            echo "Сборка упала. Смотри логи и скриншоты в артефактах."
        }
    }
}