import boto3
s3_resource = boto3.resource('s3')

''''
s3 = boto3.resource('s3',
         aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)

 '''

s3_client = boto3.client('s3')

#output to bucket
file_name='test.txt'
bucket_name = 'student5-bucket'

s3.Object('student5-bucket', file_name).upload_file(
    Filename=file_name)
