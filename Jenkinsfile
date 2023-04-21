// Simple Jenkinsfile to build CustomWiper
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m py_compile src/wiper.py'
            }
        }
        stage('Deliver') {
            steps {
                sh 'pyinstaller --onefile src/wiper.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/wiper'
                }
            }
        }
    }
}
