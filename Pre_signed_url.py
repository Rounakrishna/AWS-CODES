# its working
import boto3
import datetime

# Initialize the S3 client
s3_client = boto3.client('s3')

# Specify the bucket name and object key
bucket_name = '---------------'
object_key = '----------------'

# Generate a pre-signed URL for the S3 object
url = s3_client.generate_presigned_url(
    'get_object', 
    Params={'Bucket': bucket_name, 'Key': object_key},
    ExpiresIn=3600  # URL expiration time in seconds (e.g., 1 hour)
)

print("Pre-signed URL:", url)

