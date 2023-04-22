pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
              git branch: 'main', url: 'https://github.com/mozart-martins/test_flask_api_jenkins.git'
              echo '-----------------------------------------------------------------------'
              echo $(ls)
              echo '-----------------------------------------------------------------------'
            }
        }

        stage('Deploy') {
            environment {
                SSH_KEY = credentials('my-ssh-key')
                SSH_HOST = 'ec2-xxx-xxx-xxx-xxx.compute-1.amazonaws.com'
            }
            steps {
                sh 'scp -i $SSH_KEY -r app/ ubuntu@$SSH_HOST:/home/ubuntu/app'
                sshagent(['my-ssh-key']) {
                    sh "ssh -o StrictHostKeyChecking=no -i $SSH_KEY ubuntu@$SSH_HOST 'source /home/ubuntu/env/bin/activate && cd /home/ubuntu/app && gunicorn app:app'"
                }
            }
        }
    }
}







// pipeline {
//     agent any

//     stages {
//         stage('Build') {
//             steps {
//                 sh 'pip install -r requirements.txt'
//             }
//         }

//         stage('Deploy') {
//             steps {
//                 sh 'gunicorn app:application'
//             }
//         }
//     }
// }
