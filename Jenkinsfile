pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                sh 'git config --global --add safe.directory /var/jenkins_home/workspace/project_api_tests'
                sh 'python3 -m pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest tests/ --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }

        stage('Archive HTML Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
}