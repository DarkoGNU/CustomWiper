pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'python -m py_compile src/wiper.py'
                stash(name: 'compiled-results', includes: 'src/*.py*')
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
                }
            }
            steps {
                sh 'pyinstaller --onefile src/add2vals.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/add2vals'
                }
            }
        }
    }
}
