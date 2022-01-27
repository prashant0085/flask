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
        yum install -y httpd
        systemctl start httpd
        systemctl enable httpd
        cp -r ./html/* /var/www/html/
        systemctl restart httpd
        '''
    }
    stage('Test Deployment') {
        echo 'Deploying the Flask Application....'
    }
    stage('Notify') {
        echo 'Notifying the Deployment status....'
    }
}
