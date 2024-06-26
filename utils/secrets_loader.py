# Description: This file is responsible for loading the secret keys from the secret files.

import os


current_dir = os.path.dirname(__file__)
secrets_file_path = os.path.join(current_dir, '../.secrets')

def load_spotify_secret():
    try:
        spotify_secrets = {}
        with open(secrets_file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'SPOTIFY' in line:
                    key = line.split('=')[0].strip()
                    value = line.split('=')[1].strip()
                    spotify_secrets[key] = value
        return spotify_secrets
    except Exception as e:
        print(f'Error while loading spotify secrets: {e}')
        return None
    
    
def load_tidal_secret():
    try:
        tidal_secrets = {}
        with open(secrets_file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'TIDAL' in line:
                    key = line.split('=')[0].strip()
                    value = line.split('=')[1].strip()
                    tidal_secrets[key] = value
        return tidal_secrets
    except Exception as e:
        print(f'Error while loading tidal secrets: {e}')
        return None