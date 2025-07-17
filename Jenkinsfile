pipeline {
    agent any
    stages {
        // stage('install dependencies'){
        //     steps{
        //         sh 'pip install -r backend/requirements.txt'
        //     }  

        // }
        stage('Tests'){
            steps{
                sh '''test_app.py'''
            }
        }
    }
}