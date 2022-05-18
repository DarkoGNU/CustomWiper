pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                    args '-it --entrypoint='
                }
            }
            steps {
                echo "I'm trying my best!"
                sh "echo 'Im trying my best!'"
                sh 'python -m py_compile src/wiper.py'
            }
        }
        /*
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml src/tests.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        */
        stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python3'
                    args '-it --entrypoint='
                }
            }
            steps {
                echo "I'm trying my best!"
                sh "echo 'Im trying my best!'"
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
