from spotipy import Spotify


def filter_track_based_on_predicate(tracks_ids: list, predicate: bool) -> list:
    return [track_id for track_id in tracks_ids if predicate]
        
def get_track_feature(session: Spotify, track_id: list) -> list:
    return session.audio_features([track_id])

def get_track_camelot_key(track_feature: dict) -> str:
    
    (key, mode) = (track_feature['key'], track_feature['mode'])
    if mode == 0:
        return {
	        (0,0):'5A',
		    (1,0):'12A',
		    (2,0):'7A',
		    (3,0):'2A',
		    (4,0):'9A',
		    (5,0):'4A',
		    (6,0):'11A',
		    (7,0):'6A',
		    (8,0):'1A',
		    (9,0):'8A',
		    (10,0):'3A',
		    (11,0):'10A'
        }[key, mode]
    
    if mode == 1:
        return {
            (0,1):'8B',
            (1,1):'3B',
            (2,1):'10B',
            (3,1):'5B',
            (4,1):'12B',
            (5,1):'7B',
            (6,1):'2B',
            (7,1):'9B',
            (8,1):'4B',
            (9,1):'11B',
            (10,1):'6B',
            (11,1):'1B'
        }[key, mode]


def get_tracks_recommendation(session: Spotify, track_id: list) -> list:
    return session.recommendations(seed_tracks=track_id)


def get_track_id_from_search(session: Spotify, track_name: str) -> str:
    return session.search(track_name)['tracks']['items'][0]['id']


camelot_key_predicate = lambda track_feature, camelot_key: camelot_key  == get_track_camelot_key(track_feature)
bpm_predicate = lambda track_feature, bpm_inf, bpm_sup: (track_feature['tempo'] >= bpm_inf and track_feature['tempo'] < bpm_sup)

