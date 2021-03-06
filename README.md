# Python AWS Lambda Pulumi Example

Playing with how to set up a Python AWS Lambda using Pulumi that can talk to S3

## Pre Requisites

Each of these need to be installed and available on your path:

* [Pulumi](https://www.pulumi.com/docs/get-started/install/)
* [Python 3.8+](https://www.python.org/downloads/)
* [AWS CLI](https://aws.amazon.com/cli/)

Install the required Python packages using:

```shell
pip install -r requirements.txt
```

You'll also need to set up you local AWS credentials to be able to deploy and test the Lambda. Use this to start the wizard to set up your default local credentials:

```shell
aws configure
```

## Deployment

To create these resources in AWS run:

```shell
pulumi up
```

This is configured to use your your default AWS profile to deploy the resources to eu-west-1 (Ireland)

It will confirm with you which resources are being deployed, and ask for confirmation before continuing

## Testing the Lambda

Run the following command to send test data to the Lambda to check it is functioning

Beforehand you need to replace the `bucket_writer` function name below with the generated function name Pulumi creates (e.g: `bucket_writer-e3a935d`)

```shell
aws lambda invoke --function-name bucket_writer --region eu-west-1 --payload '{\"key1\":\"value1\", \"key2\":\"value2\", \"key3\":\"value3\"}' --cli-binary-format raw-in-base64-out test_response.txt
```

This will call the function, then create a `test_response.txt` file containing any data returned from the Lambda.


## Tearing Down the Lambda

To delete all resources run:

```shell
pulumi destroy
```

## Sources

* [Pulumi Get Started with AWS](https://www.pulumi.com/docs/get-started/aws/)
* [Writing a JSON file to an S3 bucket](https://stackoverflow.com/questions/46844263/writing-json-to-file-in-s3-bucket)
* [Pulumi AWS API Reference](https://www.pulumi.com/registry/packages/aws/api-docs/)
