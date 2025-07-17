pipeline {
    agent any
    stages {
        stage('Python Control'){
            steps{
                sh 'python --version
                    docker version
                    docker info'
            }
        }
        // stage('install dependencies'){
        //     steps{
        //         sh 'pip install -r backend/requirements.txt'
        //     }  

        // }
        // stage('Tests'){
        //     steps{
        //         sh '''test/test_app.py'''
        //     }
        // }
    }
}