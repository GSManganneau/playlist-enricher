def add_dir_to_pythonpath():
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    
add_dir_to_pythonpath()

from utils.secrets_loader import load_spotify_secret
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import MemoryCacheHandler


SECRETS = load_spotify_secret()


scope = "playlist-read-private,playlist-read-collaborative,playlist-modify-private,playlist-modify-public"


def create_spotify_session(open_browser=False):
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SECRETS["SPOTIFY_CLIENT_ID"], 
                                                     client_secret=SECRETS["SPOTIFY_CLIENT_SECRET"],
                                                     redirect_uri=SECRETS["SPOTIFY_REDIRECT_URI"],
                                                     scope=scope,
                                                     open_browser=open_browser,
                                                     cache_handler=MemoryCacheHandler()))


