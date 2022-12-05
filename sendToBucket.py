import boto3
s3_resource = boto3.resource('s3')

''''
 s3 = boto3.resource('s3',
         aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)

 '''

#output to bucket
first_file_name='test.txt'
s3_resource.Object('student5-bucket', first_file_name).upload_file(
    Filename=first_file_name)