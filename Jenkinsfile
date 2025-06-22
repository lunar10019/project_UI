pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                sh 'git config --global --add safe.directory /var/jenkins_home/workspace/project_api_tests'
                sh 'python3 -m pip install -r requirements.txt --break-system-packages'
                sh 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
                sh 'sudo apt install ./google-chrome-stable_current_amd64.deb -y'
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