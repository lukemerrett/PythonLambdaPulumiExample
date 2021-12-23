# Python AWS Lambda Pulumi Example

Playing with how to set up a Python AWS Lambda using Pulumi that can talk to S3

## Pre Requisites

Each of these need to be installed and available on your path:

* [Pulumi](https://www.pulumi.com/docs/get-started/install/)
* [Python 3.8+](https://www.python.org/downloads/)
* [AWS CLI](https://aws.amazon.com/cli/)

The Python packages you'll need are:

* [boto3](https://pypi.org/project/boto3/)

You'll also need to set up you local AWS credentials to be able to deploy and test the Lambda. Use this to start the wizard to set up your default local credentials:

```shell
aws configure
```

- [ ] Any other Pulumi pre-requisites?

## Deployment

- [ ] Deploying with Pulumi

## Testing the Lambda

Run the following command to send test data to the Lambda to check it is functioning

```shell
aws lambda invoke --function-name bucket_writer --region eu-west-1 --payload '{\"key1\":\"value1\", \"key2\":\"value2\", \"key3\":\"value3\"}' --cli-binary-format raw-in-base64-out test_response.txt
```

This will call the function, then create a `test_response.txt` file containing any data returned from the Lambda.


## Tearing Down the Lambda

- [ ] Tearing down with Pulumi

## Sources

* [Pulumi Get Started with AWS](https://www.pulumi.com/docs/get-started/aws/)
* [Writing a JSON file to an S3 bucket](https://stackoverflow.com/questions/46844263/writing-json-to-file-in-s3-bucket)
