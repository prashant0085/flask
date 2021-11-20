node {
    stage('Checkout Flask Repository') {
        checkout(
            [$class: 'GitSCM',
            branches: [[name: '*/develop']],
            browser: [$class: 'GithubWeb',
            repoUrl: 'https://github.com/prashant0085/flask'],
            extensions: [],
            userRemoteConfigs: [
                [credentialsId: 'prashant-github-access',
                url: 'https://github.com/prashant0085/flask.git']
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