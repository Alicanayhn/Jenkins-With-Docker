pipeline {
    agent any
    stages {
        stage('install dependencies'){
            steps{
                sh 'pip install -r backend/requirements.txt'
            }  

        }
        stage('Tests'){
            steps{
                sh '''python test/test_app.py'''
            }
        }
    }
}