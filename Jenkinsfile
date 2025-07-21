pipeline {
    agent any
    environment {
        VENV = 'venv'
    }
    stages {
        stage('Python Control') {
            steps {
                sh '''
                    docker version
                    docker info
                    docker container ls
                    docker network ls
                '''
            }
        }
        stage('set venv') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    . $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r backend/requirements.txt
                    pip install flake8
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    python -m unittest discover -s tests
                '''
            }
        }
        stage('Run Flake8') {
            steps {
                sh '. venv/bin/activate && flake8 . --format=default > flake8-report.txt || true'
            }
        }

        stage('Record Warnings') {
            steps {
                recordIssues tools: [flake8(pattern: 'flake8-report.txt')]
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'flake8-report.txt', allowEmptyArchive: true
        }
    }
}