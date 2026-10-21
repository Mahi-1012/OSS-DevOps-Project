
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is ready.'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover -s tests -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t oss-devops-app .'
            }
        }

        stage('Run Application') {
            steps {
                bat 'docker run --rm oss-devops-app'
            }
        }
    }
}
