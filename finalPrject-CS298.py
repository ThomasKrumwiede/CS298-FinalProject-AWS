import datetime
import boto3
import json
import requests
from urllib.request import urlopen
from flask import Flask
from flask import Flask,jsonify,request



def remove(datetime_obj):
    datetime_obj = datetime_obj.replace(".", "")
    datetime_obj = datetime_obj.replace(" ", "")
    return datetime_obj

#Create name for txt file using datetime
def createFileName():
    datetime_obj = datetime.datetime.now()
    datetime_obj = str(datetime_obj)

    file_name = remove(datetime_obj)
    return file_name


#place api output into a txt file
#url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/TESLA?format=json"
#url ="https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"

def createTxt(url, file_name):
    response = requests.get(url)
    jsondata = response.json()
    #print(json.dumps(jsondata, indent = 2,))

    print("\n*******************" * 2)

    # Get the JSON response and store it as a Python dict
    my_dictionary = requests.get(url).json()
    print(json.dumps(my_dictionary, indent=2))

    #place data in a txt file
    with open(file_name, 'w') as f:
        f.write(json.dumps(my_dictionary, indent=2))


#Place txt file into S3 bucket
def placeInbucket(file_name):
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

# Create a flask that can take arguments
final = Flask(__name__)

@final.route("/")
def welcome():
    info = "Welcome\n" + "Avalible API:\n" + "TESLA\n" + "ALLCARS"
    return info

@final.route("/ALLCARS", methods=['GET'])
def returnAll():
    url = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"
    file_name = createFileName()
    createTxt(url, file_name)
    placeInbucket(file_name)
    return file_name

@final.route("/TESLA", methods=['GET'])
def returnTESLA():
    url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/TESLA?format=json"
    file_name = createFileName()
    createTxt(url, file_name)
    placeInbucket(file_name)
    return file_name

if __name__ == '__main__':
    final.run(host="0.0.0", port=8080)