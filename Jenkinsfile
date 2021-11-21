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
                string(
                    name: 'GITHUB_REPO_BRANCH',
                    defaultValue: 'develop',
                    description: 'Github repository branch',
                    trim: true
                ),
                pipelineTriggers(
                    [githubPush()]
            )
        ]
    )

    stage('Checkout Flask Repository') {
        checkout(
            [$class: 'GitSCM',
            branches: [[name: ${params.GITHUB_REPO_BRANCH}],
            browser: [$class: 'GithubWeb',
            repoUrl: ${params.GITHUB_REPO_URL}],
            extensions: [],
            userRemoteConfigs: [
                [credentialsId: 'prashant-github-access',
                url: ${params.GITHUB_REPO_URL}]
                ]
            ]
        )
    }
    stage('Deploy the code') {
        echo 'Deploying Flask Application....'
    }
    stage('Test Deployment') {
        echo 'Deploying the Flask Application....'
    }
    stage('Notify') {
        echo 'Notifying the Deployment status....'
    }
}