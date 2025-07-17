pipeline {
    agent any
    environment{
        VENV = 'venv'
    }
    stages {
        stage('Python Control'){
            steps{
                sh '''
                    docker version
                    docker info
                '''  
            }
        }
        // stage('install dependencies'){
        //     steps{
        //         sh 'pip install -r backend/requirements.txt'
        //     }  

        // }
        stage('set venv'){
            steps{
                bat 'python -m venv %VENV%'
                bat '%VENV%\\Scripts\\python -m pip install --upgrate pip'
                bat '½VENV%\\Scripts\\pip install -r backend/requirements.txt'
            }
        }
        stage('Tests'){
            steps{
                bat '%VENV%\\Scripts\\python -m unittest discover -s tests'
            }
        }
    }
}