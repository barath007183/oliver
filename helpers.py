import boto3

CLAUDE_V3_SONNET_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"
CLAUDE_V3_HAIKU_MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"


def get_client(
    access_key_id: str,
    secret_access_key: str,
    region: str,
    service: str = "bedrock-runtime",
):
    # If access key and secret access key are provided, use them to create a session
    if access_key_id and secret_access_key:
        boto_session = boto3.Session(
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            region_name=region,
        )
        boto_client = boto_session.client(service)
    else:
        # get client using default credentials
        boto_session = boto3.Session()
        boto_client = boto_session.client(service, region_name=region)
    return boto_client
