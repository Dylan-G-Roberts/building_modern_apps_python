import boto3

client = boto3.client('s3')

response == client.list_objects(Bucket='aws-bma-testing')

for content in response['Contents']:
    obj_dict = client.get_object(Bucket='aws-bma-testing', Key=content['Key'])
    print(content['Key'], object_dict['LastModified'])
