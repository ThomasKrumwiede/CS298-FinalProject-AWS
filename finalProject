import datetime
import boto3
import json
import requests
from urllib.request import urlopen

#Create name for txt file using datetime
datetime_obj = datetime.datetime.now()

datetime_obj = str(datetime_obj)

def remove(datetime_obj):
    return datetime_obj.replace(" ", "")

file_name = remove(datetime_obj)

print (file_name)


#place api output into a txt file
url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/TESLA?format=json"

#url ="https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"

response = requests.get(url)
jsondata = response.json()
#print(json.dumps(jsondata, indent = 2,))


print("\n*******************" * 2)

"""
Dictionaries map keys to values and store them in an array or collection.
The keys must be of a hashable type, which means that they must have a hash value that never changes during the key’s lifetime.
"""

# Get the JSON response and store it as a Python dict
my_dictionary = requests.get(url).json()
print(json.dumps(my_dictionary, indent=2))

#place data in a text file
with open(file_name, 'w') as f:
    f.write(json.dumps(my_dictionary, indent=2))


#Place txt file into S3 bucket
s3_resource = boto3.resource('s3')

''''
s3 = boto3.resource('s3',
         aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)
 '''

s3_client = boto3.client('s3')

#output to bucket
bucket_name = 'student5-bucket'

s3.Object('student5-bucket', file_name).upload_file(
    Filename=file_name)
