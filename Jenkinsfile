pipeline {
    agent any
    stages {
        stage('Build and Test') {
            steps {
                checkout scm
                sh 'echo "Starting tests..."'
                sh 'python3 test.py'
            }
        }
    }
}
