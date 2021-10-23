import requests

# Insert user
data = {
    'email': 'admin1@dandyhacks.com',
    'username': 'admin1',
    'password': 'P@ssw0rd',
    'points': 0,
}

print(requests.post('http://127.0.0.1:5000/insertUser/', data=data).text)

# Insert Location
data = {
    'user': 'admin1',
    'longitude': '101298301',
    'latitude': '297872934',
    'image': 'test',
    'comment': 'clean clean clean',
    'type': '0',
    'title': 'Some place'
}

print(requests.post('http://127.0.0.1:5000/insertLocation/', data=data).text)

# String to json
import json

achievements = {
        "beHuman": [False, "You are human!", 100],
        "environmentalist": [False, "You completed your first cleanup activity!", 100],
        "warrior": [False, "You completed your first 5 cleanup activities!", 300],
        "cleanup warlock": [False, "You completed your first 10 cleanup activities!", 500],
    }

print(json.dumps(achievements))


# Upload / Download photo
from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_.json_credential_file"

def upload_blob(bucket_name, source_file_name, destination_blob_name):

    storage_client = storage.Client("Dandy Bois")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

def download_blob(bucket_name, source_file_name, destination_file_name):

    storage_client = storage.Client("Dandy Bois")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_file_name)

    blob.download_to_filename(destination_file_name)

    print(
        "File {} downloaded to {}.".format(
            source_file_name, destination_file_name
        )
    )

upload_blob("Dandy Bois Bucket 1", 'star.png', 'starOnServer.png')

