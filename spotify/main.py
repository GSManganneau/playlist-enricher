from sessionManager import create_spotify_session
from playlistManager import get_all_playlists, get_playlist_names, get_playlist_id, get_tracks_from_playlist, get_random_tracks_sample_from_playlist, get_tracks_ids_from_tracks
from trackManager import filter_track_based_on_predicate, get_track_feature, get_tracks_recommendation, camelot_key_predicate, bpm_predicate

import yaml
import os



current_dir = os.path.dirname(__file__)
config_file_path = os.path.join(current_dir, 'playlists_conf.yml')

def get_yaml_config():
    with open(config_file_path) as f:
        return yaml.load(f, Loader=yaml.FullLoader)

conf = get_yaml_config()

if __name__ == '__main__':
    
    session = create_spotify_session(True)
    
    for playlist in conf['playlists_to_use_for_recommendation']:
        print(f"Playlist: {playlist}")
        playlist_id = get_playlist_id(session, playlist)
        print(("==================="))
        print((f"Playlist_id: {playlist_id}"))
        print(("==================="))
        tracks = get_random_tracks_sample_from_playlist(session, playlist_id)
        tracks_ids = get_tracks_ids_from_tracks(tracks)
        tracks_recommendations = get_tracks_recommendation(session, tracks_ids[0:3])
        print(tracks_recommendations)
        recommended_tracks_ids = [track['id'] for track in tracks_recommendations['tracks']]
        
        for track_id in recommended_tracks_ids:
            track_features = get_track_feature(session, track_id)
            
            print(f"Track: {track_id}")
            print(f"Features: {track_features}")
            camelot_key = "12A"
            if filter_track_based_on_predicate(track_features, camelot_key_predicate(track_features[0], camelot_key)):
                
                playlist_name = f'{camelot_key} - To Approve'
                playlist_id = get_playlist_id(session, playlist_name)
                
                session.playlist_add_items(playlist_id, [track_id])


                