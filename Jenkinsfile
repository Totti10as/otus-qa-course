pipeline {
         agent{
             docker { image 'my_ubuntu_v1'}
         }
         stages{
            stage('Code pull'){
                steps{
                    checkout scm
                }
            }
            stage('Run pep8')
              {
                steps{
                    sh 'pep8 less2/tests/test_section3.py'
                }
            }
         }