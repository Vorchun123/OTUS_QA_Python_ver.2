pipeline {
    agent { label 'windows' }
    options {
        timeout(time: 20, unit: 'MINUTES')
    }
    environment {
        MYSQL_ROOT_PASSWORD = credentials('prestashop-mysql-root-password')
        ADMIN_PASSWD        = credentials('prestashop-admin-password')
        COMPOSE_PROJECT_NAME = "otus-qa-${BUILD_NUMBER}"
        PS_DOMAIN            = "localhost:8081"
        WORKSPACE_UNIX       = ""
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Prepare') {
            steps {
                script {
                    bat '''
                        docker version
                        docker compose version
                        docker network create selenoid1 || exit 0
                        docker network create selenoid2 || exit 0
                    '''
                }
            }
        }
        stage('Build test image') {
            steps {
                dir('docker_selenoid') {
                    bat '''
                        docker compose -f docker-compose.yml -f docker-compose.ci.yml build tests
                    '''
                }
            }
        }
        stage('Start infra') {
            steps {
                dir('docker_selenoid') {
                    bat '''
                        docker compose -f docker-compose.yml -f docker-compose.ci.yml up -d ^
                            db prestashop prestashop_postinstall ^
                            selenoid1 selenoid2 ggr ggr_ui selenoid_ui nginx
                    '''
                }
            }
        }
        stage('Wait for PrestaShop') {
            steps {
                dir('docker_selenoid') {
                    bat '''
                        docker wait %COMPOSE_PROJECT_NAME%_prestashop_postinstall_1
                    '''
                }
            }
        }
        stage('Run tests') {
            steps {
                dir('docker_selenoid') {
                    bat 'if exist reports rmdir /S /Q reports'
                    bat 'mkdir reports'
                    bat '''
                        docker compose -f docker-compose.yml -f docker-compose.ci.yml ^
                            run --rm tests
                    '''
                }
            }
        }
    }
    post {
        always {
            dir('docker_selenoid') {
                bat '''
                    docker compose -f docker-compose.yml -f docker-compose.ci.yml logs --no-color > reports\\compose.log 2>&1 || exit 0
                '''
            }
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'docker_selenoid/reports']]
            archiveArtifacts artifacts: 'docker_selenoid/reports/**',
                             allowEmptyArchive: true
            dir('docker_selenoid') {
                bat '''
                    docker compose -f docker-compose.yml -f docker-compose.ci.yml down -v --remove-orphans || exit 0
                '''
            }
        }
    }
}