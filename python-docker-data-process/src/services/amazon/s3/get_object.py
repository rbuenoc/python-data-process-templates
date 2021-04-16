from .base import create_s3_service_client


def get_object(bucket_name, key) -> bytes:
    s3 = create_s3_service_client()
    response = s3.get_object(Bucket=bucket_name, Key=key)
    _validate_response(response)
    body = response.get('Body')
    return _process_body(body) if body else None


def _process_body(body):
    return body.read()


def _validate_response(response):
    if not response.get('Body'):
        raise ValueError("Response does not contains the key 'Body'")
