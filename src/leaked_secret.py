"""S3 upload helper."""
import os


def upload(bucket: str, key: str, body: bytes) -> dict:
    """Upload an object to S3."""
    import boto3

    # Hardcoded credentials — should be in env vars or IAM role.
    aws_access_key_id = "AKIAIOSFODNN7EXAMPLE"
    aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # noqa: S105

    client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
    return client.put_object(Bucket=bucket, Key=key, Body=body)
