from spotipy import Spotify
from spotify.camelotKeyModelManager import get_camelot_key_from_model


def filter_track_based_on_predicate(tracks_ids: list, predicate: bool) -> list:
    return [track_id for track_id in tracks_ids if predicate]
        
def get_track_feature(session: Spotify, track_id: list) -> list:
    try:
        audio_features = session.audio_features(track_id)
        return audio_features
    except Exception as e:
        #print("Error: ", e)
        return None

def get_track_camelot_key(track_feature: dict) -> str:
    return get_camelot_key_from_model(track_feature)

def get_tracks_recommendation(session: Spotify, track_id: list) -> list:
    return session.recommendations(seed_tracks=track_id)


def get_track_id_from_search(session: Spotify, track_name: str) -> str:
    return session.search(track_name)['tracks']['items'][0]['id']


camelot_key_predicate = lambda track_feature, camelot_key: camelot_key  == get_track_camelot_key(track_feature)
bpm_predicate = lambda track_feature, bpm_inf, bpm_sup: (track_feature['tempo'] >= bpm_inf and track_feature['tempo'] < bpm_sup)

