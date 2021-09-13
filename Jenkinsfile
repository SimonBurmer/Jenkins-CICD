pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pip install -r requirements.txt' /* pip has to be installed on EC2 and addad to PATH!*/
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python test.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
