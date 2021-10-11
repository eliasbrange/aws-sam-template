# aws-sam-template

## 1. Fork this repository

## 2. Create GitHub environments

- development
- stage
- production

## 3. Install AWS SAM CLI

```shell script
$ pip3 install aws-sam-cli
```

## 4. Bootstrap sam resources for each environment

Use SAM CLI to bootstrap required infrastructure resources. 
It would probably be a good idea keep the different environments in different AWS accounts, 
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

## 5. Add secrets to GitHub environments

For each environment, add the following secrets:

- **AWS_ACCESS_KEY_ID**: From the credentials shown in the bootstrap output.
- **AWS_SECRET_ACCESS_KEY**: From the credentials shown in the bootstrap output.
- **SAM_BUCKET**: The artifact bucket created for each environment by the bootstrap script.
- **PIPELINE ROLE**: The pipeline execution role created for each environment by the bootstrap script.
- **DEPLOY_ROLE**: The CloudFormation execution role for each environment by the bootstrap script.

> If the bootstraps from step #4 were performed in the same account, only one IAM user will have been created.
> In that case, use the same credentials in all accounts.

## 6. Deploy to development

Deployment to development is made by the *DevDeploy* workflow, which can be manually triggered.

## 7. Deploy to stage & production

Deployment to stage and production is made by the *StageProdDeploy* workflow, which is triggered whenever a GitHub release is published.
