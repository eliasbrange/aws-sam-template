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

```shell script
$ sam pipeline bootstrap --stage dev
$ sam pipeline bootstrap --stage stage
$ sam pipeline bootstrap --stage prod
```

> Above should preferably be done in three different AWS accounts.

## 5. Add credentials to GitHub secrets

Each bootstrap above will give you one set of access keys. 
These should be added as secrets under the respective GitHub environment.

> If the above bootstraps were performed in the same account, only one IAM user will have been created.
