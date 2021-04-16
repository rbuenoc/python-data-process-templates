import boto3

class AmazonService:
    S3 = 's3'


def create_service_client(amazon_service, **args):
    return boto3.client(amazon_service, **args)


def create_service_resource(amazon_service, **args):
    return boto3.resource(amazon_service, **args)
