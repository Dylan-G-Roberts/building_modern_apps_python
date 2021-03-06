import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('aws-bma-testing')

for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)

s3_client = boto3.resource('s3').meta.client
