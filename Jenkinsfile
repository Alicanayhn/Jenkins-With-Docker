pipeline {
    agent any
    stages {
        stage('verify tooling') {
            steps{
                sh '''
                    // docker compose up --build
                '''
            }
        }
        stage('install dependencies'){
            steps{
                sh ''' pip install -r backend/requirements.txt'''
            }  

        }
        stage('Tests'){
            steps{
                sh '''python test/test_app.py'''
            }
        }
    }
}