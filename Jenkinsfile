pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS_ID = 'dockerhub-credentials-id'
        repoDockerHub = 'margus23'
        nameContainer = 'api-test-exam'
        GIT_CREDENTIALS_ID = 'git-credentials-id'
        GITHUB_TOKEN = credentials('github-token')
    }

    stages {
        stage('Clonar Repositorio') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/martinlopez5/examen-devops-2024.git',
                    credentialsId: env.GIT_CREDENTIALS_ID
            }
        }
        
        stage('Build - Construir imagen Docker') {
            steps {
                script {
                    // Obtener el ultimo tag
                    def lastTag = sh(script: "git describe --tags --abbrev=0 origin/main", returnStdout: true).trim()
                    // Construir imagen Docker con el tag obtenido
                    sh "docker build -t ${env.repoDockerHub}/${env.nameContainer}:${lastTag} ./app"
                }
            }
        }
        
        stage('Subir imagen a Docker Hub') {
            steps {
                script {
                    def lastTag = sh(script: "git describe --tags --abbrev=0 origin/main", returnStdout: true).trim()

                    // Obtener las credenciales de Docker Hub
                    def dockerCredentials = withCredentials([usernamePassword(credentialsId: env.DOCKERHUB_CREDENTIALS_ID, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) {
                        return [
                            username: env.DOCKER_USER,
                            password: env.DOCKER_PASSWORD
                        ]
                    }

                    // Login a Docker Hub utilizando el método seguro --password-stdin
                    sh "echo ${dockerCredentials.password} | docker login -u ${dockerCredentials.username} --password-stdin"

                    // Subir la imagen
                    sh "docker push ${env.repoDockerHub}/${env.nameContainer}:${lastTag}"
                }
            }
        }

        
        stage('Actualizar Kubernetes Deployment') {
            steps {
                script {

                    def lastTag = sh(script: "git describe --tags --abbrev=0 origin/main", returnStdout: true).trim()
                    // Usa un comando sed apropiado para tu entorno y verifica la ruta del archivo
                    sh """
                    bash -c "sed -i 's|^\\(\\s*\\)image:.*|\\1image: ${env.repoDockerHub}/${env.nameContainer}:${lastTag}|' manifest/Deployment.yaml"
                    """

                    // Git commit y push los cambios
                    withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                        sh """
                        git config user.email 'martingustavolopez@gmail.com'
                        git config user.name 'martinlopez5'
                        git add manifest/Deployment.yaml
                        git commit -m 'Update image tag to ${lastTag} '
                        git remote set-url origin https://\${GITHUB_TOKEN}@github.com/martinlopez5/examen-devops-2024.git
                        git push origin main
                        """
                    }
                }
            }
        }

        stage('Limpiar Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Docker logout'){
            steps{
                sh "docker logout"
            }
        }
    }
}