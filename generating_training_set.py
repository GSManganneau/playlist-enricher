
import os

current_dir = os.path.dirname(__file__)
os.environ['PYTHONPATH'] = current_dir

from spotify.sessionManager import create_spotify_session
from spotify.playlistManager import get_tracks_from_playlist, get_playlist_id
from spotify.trackManager import get_track_feature, get_track_camelot_key, filter_track_based_on_predicate, camelot_key_predicate, bpm_predicate


result = []

playlists = [
"12B",
"12A",
"11B",
"11A",
"10A",
"10B",
"9A",
"9B",
"8B",
"8A",
"7B",
"7A",
"6B",
"6A",
"5B",
"5A",
"4B",
"4A",
"3A",
"3B",
"2A",
"2B",
"1A",
"1B"
]

session = create_spotify_session(True)


for playlist in playlists:
    
    playlist_id = get_playlist_id(f"{playlist}")
    tracks_from_playlist = get_tracks_from_playlist(session, playlist_id)
    

    for track in tracks_from_playlist:
        
        track_name = track['track']['name']
        track_id = track['track']['id']
        
        track_features = get_track_feature(session, track_id)
        
        if track_features is not None:
            if track_features[0] is not None:
            
                track_key = track_features[0]['key']
                track_mode = track_features[0]['mode']
                track_acousticness = track_features[0]['acousticness']
                track_danceability = track_features[0]['danceability']
                track_energy = track_features[0]['energy']
                track_instrumentalness = track_features[0]['instrumentalness']
                track_key = track_features[0]['key']
                track_liveness = track_features[0]['liveness']
                track_loudness = track_features[0]['loudness']
                track_speechiness = track_features[0]['speechiness']
                track_time_signature = track_features[0]['time_signature']
                track_valence = track_features[0]['valence']
                
                
                result.append({
                    "track_name": track_name,
                    "track_id": track_id,
                    "track_key" : track_key,
                    "track_mode" : track_mode,
                    "track_acousticness" : track_acousticness,
                    "track_danceability" : track_danceability,
                    "track_energy" : track_energy,
                    "track_instrumentalness" : track_instrumentalness,
                    "track_speechiness" : track_speechiness,
                    "track_liveless" : track_liveness,
                    "track_loudness" : track_loudness,
                    "track_time_signature" : track_time_signature,
                    "track_valence" : track_valence,
                    "djayPro_key": playlist
                })

            
with open('training_set.json', 'w') as f:
    import json
    f.write(json.dumps(result))
