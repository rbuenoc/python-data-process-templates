from services.amazon.base import create_service_client, create_service_resource, AmazonService


def create_s3_service_client(**args):
    return create_service_client(AmazonService.S3, **args)


def create_s3_service_resource(**args):
    return create_service_resource(AmazonService.S3, **args)
