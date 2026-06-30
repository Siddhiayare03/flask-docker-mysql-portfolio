pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up --build -d'
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 10'
                sh 'curl http://localhost:5000'
            }
        }

    }

    post {
        success {
            echo 'Deployment Successful!'
        }

        failure {
            echo 'Deployment Failed!'
        }
    }
}