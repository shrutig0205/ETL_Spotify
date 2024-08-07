import json
import pandas as pd

def process_spotify_response(tracks):

    songs = []  
    # Iterate over each track and extract relevant details
    for track in tracks:
        song_details = {
            "song_id": track.get("id"),
            "song_name": track.get("name"),
            "song_type": track.get("type"),
            "duration_ms": track.get("duration_ms"),
            "popularity": track.get("popularity"),
            "artists": ", ".join([artist.get("name") for artist in track.get("artists", [])]),
            "album_type": track.get("album", {}).get("album_type"),
            "album_name": track.get("album", {}).get("name"),
            "album_id": track.get("album", {}).get("id"),
            "release_date": track.get("album", {}).get("release_date"),
            "spotify_url": track.get("external_urls", {}).get("spotify")
        }
        songs.append(song_details)
        
    song_df = pd.DataFrame(songs)
    return song_df

with open('indian_indie_songs.json', 'r') as file:
    data = json.load(file)

songs_data_df = process_spotify_response(data)
print(songs_data_df)

songs_data_df.to_csv("songs_list.csv",index=False)