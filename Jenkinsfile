pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                // Use pip3 to install your dependencies
                sh 'pip3 install pytest'
            }
        }
        stage('Run Tests') {
            steps {
                // Now run pytest
                sh 'pytest'
            }
        }
    }
}
