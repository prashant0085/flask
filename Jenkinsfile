node {
    properties(
        [parameters(
            [
                string(
                    name: 'GITHUB_REPO_URL',
                    defaultValue: 'https://github.com/prashant0085/flask.git',
                    description: 'GitHub repository URL',
                    trim: true
                ),
                choice(
                    choices: ['develop', 'main', 'master'],
                    description: 'Github repository branch',
                    name: 'GITHUB_REPO_BRANCH')]
                ),
                pipelineTriggers(
                    [githubPush()]
            )
        ]
    )

    stage('Checkout Flask Repository') {
        checkout(
            [$class: 'GitSCM',
            branches: [[name: "${params.GITHUB_REPO_BRANCH}"]],
            browser: [$class: 'GithubWeb',
            repoUrl: "${params.GITHUB_REPO_URL}"],
            extensions: [],
            userRemoteConfigs: [
                [credentialsId: 'prashant-github-access',
                url: "${params.GITHUB_REPO_URL}"]
                ]
            ]
        )
    }
    stage('Deploy the code') {
        echo 'Deploying Flask Application....'
        sh '''
        ls -la
        #!/bin/bash
        yum update -y
        amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
        yum install -y httpd mariadb-server
        systemctl start httpd
        systemctl enable httpd
        usermod -a -G apache ec2-user
        chown -R ec2-user:apache /var/www
        chmod 2775 /var/www
        find /var/www -type d -exec chmod 2775 {}
        find /var/www -type f -exec chmod 0664 {}
        echo "Hello-World" > /var/www/html/index.html
        '''
    }
    stage('Test Deployment') {
        echo 'Deploying the Flask Application....'
    }
    stage('Notify') {
        echo 'Notifying the Deployment status....'
    }
}
