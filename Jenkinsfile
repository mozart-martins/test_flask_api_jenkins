pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mozart-martins/test_flask_api_jenkins'
            }
        }
        stage('Pre-build') {
            steps {
                sh 'sudo su'
                sh 'apt-get update'
                sh 'apt-get install python3-pip -y'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build and Test') {
            steps {
                sh 'pytest test_api.py'
            }
        }
        stage('Post-build') {
            steps {
                sh 'tar -czvf myapp.tar.gz .'
            }
        }
    }
}
