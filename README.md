# AWS SAM Template

A simple template to deploy an AWS SAM application in three different environments using GitHub Actions.
The template deploys a single AWS Lambda function that returns a random quote from https://api.quotable.io when invoked.

## Setup
### 1. Use this repository as a template

### 2. Create GitHub environments

- development
- stage
- production

### 3. Install AWS SAM CLI

```shell script
$ pip3 install aws-sam-cli
```

### 4. Bootstrap infrastructure
Use [SAM CLI to bootstrap](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-pipeline-bootstrap.html) required infrastructure resources. 
It would be preferable to bootstrap the different environments in different AWS accounts, 
but for testing purposes they can all be bootstrapped into the same account.

```shell script
$ sam pipeline bootstrap --stage dev
...
The following resources were created in your account:
	- Pipeline IAM user
	- Pipeline execution role
	- CloudFormation execution role
	- Artifact bucket
Pipeline IAM user credential:
	AWS_ACCESS_KEY_ID: XXXX
	AWS_SECRET_ACCESS_KEY: XXXX

$ sam pipeline bootstrap --stage stage
...

$ sam pipeline bootstrap --stage prod
...
```
### 5. Add secrets to GitHub environments

For each environment, add the following secrets:

- **AWS_ACCESS_KEY_ID**: From the credentials shown in the bootstrap output.
- **AWS_SECRET_ACCESS_KEY**: From the credentials shown in the bootstrap output.
- **SAM_BUCKET**: The artifact bucket created for each environment by the bootstrap script.
- **PIPELINE ROLE**: The pipeline execution role created for each environment by the bootstrap script.
- **DEPLOY_ROLE**: The CloudFormation execution role for each environment by the bootstrap script.

> If the bootstraps from step #4 were performed in the same account, only one IAM user will have been created.
> In that case, use the same credentials in all environments.

## Deploy

Deployment to the different environments is handled by two different GitHub Actions workflows.

### 1. Deploy to development

Deployment to development is made by the *DevDeploy* workflow, which can be manually triggered.

### 2. Deploy to stage & production

Deployment to stage and production is made by the *StageProdDeploy* workflow, which is triggered whenever a GitHub release is published.
