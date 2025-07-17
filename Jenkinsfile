pipeline {
    agent any
    stages {
        stage('verify tooling') {
            steps{
                sh '''
                    docker compose up --build
                '''
            }
        }
    }
}