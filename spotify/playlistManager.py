from spotipy import Spotify
from spotify.sessionManager import create_spotify_session


def read_playlist(session: Spotify, playlist_id: str) -> dict:
    return session.playlist(playlist_id)

def get_all_playlists(session: Spotify) -> list:
    return session.current_user_playlists(limit=50)

def get_playlist_names(session: Spotify) -> list:
    playlists = get_all_playlists(session)['items']
    return [playlist['name'] for playlist in playlists]

def get_playlist_id(playlist_name: str) -> str:
    from spotify.playlist_mapping import PLAYLIST_MAP
    return PLAYLIST_MAP[playlist_name]

def get_tracks_from_playlist(session: Spotify, playlist_id: str) -> list:
    playlist = read_playlist(session, playlist_id)
    return playlist['tracks']['items']


def get_random_tracks_sample_from_playlist(session: Spotify, playlist_id: str) -> list:
    import random
    playlist = read_playlist(session, playlist_id)
    tracks = playlist['tracks']['items']
    max_sample_size = len(tracks)
    random_number = random.randint(0, max_sample_size)
    return random.sample(tracks, random_number)

def get_tracks_ids_from_tracks(tracks: list) -> list:
    return [track['track']['id'] for track in tracks]




playlists = get_all_playlists(create_spotify_session(True))

for playlist in playlists['items']:
    print(f"{playlist['name']} : {playlist['id']}") 
    