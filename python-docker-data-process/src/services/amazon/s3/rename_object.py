from .base import create_s3_service_resource

def rename_object(bucket_name, old_key, new_key):
    s3 = create_s3_service_resource()
    s3.Object(bucket_name, new_key).copy_from(CopySource=bucket_name + '/' + old_key)
    s3.Object(bucket_name, old_key).delete()
