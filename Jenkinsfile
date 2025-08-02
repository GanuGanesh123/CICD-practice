pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                // It's good practice to create a virtual environment first.
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'

                // Install pytest. You should also install your project's dependencies here.
                sh 'pip install pytest'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate'
                sh 'pytest'
            }
        }
    }
}
