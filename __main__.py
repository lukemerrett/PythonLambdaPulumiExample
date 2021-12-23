import json
import pulumi
import pulumi_aws as aws

bucket = aws.s3.Bucket("bucket-writer-sample")

access_bucket_policy = aws.iam.Policy(
    "access_bucket_policy",
    policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": ["s3:*"],
            "Resource": f"arn:aws:s3:::bucket-writer-sample*"
        }],
    })
)

role_for_lambda = aws.iam.Role(
    "lambda_exec",
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "lambda.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }]
    }),
    managed_policy_arns=[access_bucket_policy.arn]
)

aws_lambda = aws.lambda_.Function(
    "bucket_writer",
    code=pulumi.FileArchive("./src"),
    role=role_for_lambda.arn,
    handler="lambda.handler",
    runtime="python3.9",
    environment=aws.lambda_.FunctionEnvironmentArgs(
        variables={
            "BUCKET_NAME": bucket.id
        }
    )
)

# Export the name of the bucket
pulumi.export("bucket_name", bucket.id)
pulumi.export("lambda_name", aws_lambda.id)
