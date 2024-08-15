# load.py
import os
import boto3
from datetime import datetime

now_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
s3_bucket_name = os.getenv("S3_BUCKET_NAME")
s3_file_key = f"spotify_data/indie_songs_{now_time}.csv"

def upload_to_s3(file_path, bucket_name, file_key):
    s3_client = boto3.client(
        's3'
    )
    s3_client.upload_file(file_path, bucket_name, file_key)
    print(f"Uploaded CSV file to S3 at s3://{bucket_name}/{file_key}")

if __name__ == "__main__":
    upload_to_s3('songs_list.csv', s3_bucket_name, s3_file_key, aws_access_key_id, aws_secret_access_key)

