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
                    docker network ls --all
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
    }
}