import json
import os
from datetime import datetime
from extract_spotify_data import get_token, search_indian_indie_songs
from transform_spotify_data import process_spotify_response
from load_spotify_data import upload_to_s3

def lambda_handler(event, context):
    print("Received Event:",event)
    try:
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")
        s3_bucket_name = os.getenv("S3_BUCKET_NAME")

        # Extract
        token = get_token()
        print("Token generated.")
        songs = search_indian_indie_songs(token)
        print("Raw songs data",songs)

        # Transform
        df = process_spotify_response(songs)
        print("Transformed Data",df)
        csv_file_path = "/tmp/songs_list.csv"
        df.to_csv(csv_file_path, index=False)

        # Load
        now_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        s3_file_key = f"spotify_data/indie_songs_{now_time}.csv"
        upload_to_s3(csv_file_path, s3_bucket_name, s3_file_key)
        print("csv saved in S3",csv_file_path)
        print("Bucket Name",s3_bucket_name)
        print("S3 File Key",s3_file_key)

        return {
            'statusCode': 200,
            'body': json.dumps('ETL Pipeline executed successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error executing ETL pipeline: {str(e)}')
        }