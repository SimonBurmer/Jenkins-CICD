pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '/usr/bin/pip3 install -r requirements.txt' /* pip has to be installed on EC2!*/
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
