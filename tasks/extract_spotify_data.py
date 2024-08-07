import base64
import json
import os

from dotenv import load_dotenv
from requests import get, post

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(client_id, client_secret)


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    print(json_result)
    token = json_result["access_token"]
    return token


TOKEN = get_token()


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=10"

    query_url = url + query

    result = get(query_url, headers=headers)

    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None
    return json_result[0]


def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country-IN"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


def search_indian_indie_songs(token, days=30):
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": "Bearer " + token}
    query = "tag:hindi%20tag:indie%20tag:new%20year:2024"
    params = {"q": query, "type": "track", "limit": 20}
    response = get(url, headers=headers, params=params)
    response_data = response.json()
    return response_data["tracks"]["items"]


# result = search_for_artist(token, "Arijit Singh")
# artist_id = result["id"]
# songs = get_songs_by_artist(token, artist_id)

# for idx, song in enumerate(songs):
#     print(f"{idx + 1}. {song ['name']}")

try:
    songs = search_indian_indie_songs(TOKEN, days=30)
except Exception as e:
    TOKEN = get_token()
    songs = search_indian_indie_songs(TOKEN, days=30)

with open("indian_indie_songs.json", "w", encoding="utf-8") as f:
    json.dump(songs, f, ensure_ascii=False, indent=4)

for idx, song in enumerate(songs):
    artists = song["artists"]
    artists = ", ".join([artist["name"] for artist in artists])
    print(f"{idx + 1}. {song ['name']} - {artists}")
