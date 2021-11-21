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
        python3 --version
        sudo su
        yum install nodejs -y
        npm install pm2@latest -g
        pip3 install virtualenv
        virtualenv --python=python3 venv
        source ./venv/bin/activate
        pip3 install -r requirements.txt
        pm2 start flaskblog.py --name flaskblog-app --interpreter=python3
        '''
    }
    stage('Test Deployment') {
        echo 'Deploying the Flask Application....'
    }
    stage('Notify') {
        echo 'Notifying the Deployment status....'
    }
}