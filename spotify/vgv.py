from sessionManager import create_spotify_session
from playlistManager import get_tracks_from_playlist, get_playlist_id
from trackManager import get_track_feature, get_track_camelot_key, filter_track_based_on_predicate, camelot_key_predicate, bpm_predicate


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
        
        if track_features[0] is not None:
        
            track_key = track_features[0]['key']
            track_mode = track_features[0]['mode']
            camelot_key = get_track_camelot_key(track_features[0])
            
            result.append({
                "track_name": track_name,
                "track_id": track_id,
                "track_key": track_key,
                "track_mode": track_mode,
                "camelot_key": camelot_key,
                "djayPro_key": playlist
            })
        else:
            result.append({
                "track_name": track_name,
                "track_id": track_id,
                "track_key": "None",
                "track_mode": "None",
                "camelot_key": "None",
                "djayPro_key": playlist
            })
            
with open('key_analysis.json', 'w') as f:
    f.write(str(result))
    
    
        #print(f"Track {track_name} has key {track_key} and mode {track_mode} which corresponds to Camelot key {camelot_key}")
        
        #playlist_id = get_playlist_id(f"{camelot_key}")
        
        #print(f"Adding track {track_name} to playlist {camelot_key}")
        
        #session.playlist_add_items(playlist_id, [track_id])
        
        #print(f"Track {track_name} added to playlist {camelot_key}")
        
        #track_bpm = track_features[0]['tempo']
        #print(f"Track {track_name} has {track_bpm} BPM")
        
    # if track_bpm >= 90 and track_bpm < 100:
    #     playlist_id = get_playlist_id("BPM 90-100")
    #     print(f"Adding track {track_name} to playlist 90-100 BPM")
    #     session.playlist_add_items(playlist_id, [track_id])
    #     print(f"Track {track_name} added to playlist 90-100 BPM")
    # 
    # if track_bpm >= 100 and track_bpm < 110:
    #     playlist_id = get_playlist_id("BPM 100-110")
    #     print(f"Adding track {track_name} to playlist 100-110 BPM")
    #     session.playlist_add_items(playlist_id, [track_id])
    #     print(f"Track {track_name} added to playlist 100-110 BPM")
    #     
    # if track_bpm >= 110 and track_bpm < 120:
    #     playlist_id = get_playlist_id("BPM 110-120")
    #     print(f"Adding track {track_name} to playlist 110-120 BPM with ID {playlist_id}")
    #     session.playlist_add_items(playlist_id, [track_id])
    #     print(f"Track {track_name} added to playlist 110-120 BPM")
    # 
    # if track_bpm >= 120 and track_bpm < 130:
    #     playlist_id = get_playlist_id("BPM 120-130")
    #     print(f"Adding track {track_name} to playlist 120-130 BPM")
    #     session.playlist_add_items(playlist_id, [track_id])
    #     print(f"Track {track_name} added to playlist 120-130 BPM")
    #     
    # if track_bpm >= 130 and track_bpm < 140:
    #     playlist_id = get_playlist_id("BPM 130-140")
    #     print(f"Adding track {track_name} to playlist 130-140 BPM")
    #     session.playlist_add_items(playlist_id, [track_id])
    #     print(f"Track {track_name} added to playlist 130-140 BPM")
    #     
    # if track_bpm >= 140:
    #     playlist_id = get_playlist_id("BPM 140+")
    #     print(f"Adding track {track_name} to playlist 140+ BPM")
    #     session.playlist_add_items(playlist_id, [track_id])
    #     print(f"Track {track_name} added to playlist 140+ BPM")
    # 
