import json
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'key_mode_class_distribution.json')

def load_model():
    with open(model_path, 'r') as f:
        return json.load(f)
    
def get_camelot_key_from_model(track_feature: dict) -> str:

    key_mode_class_distribution = load_model()


    key = track_feature['key']
    mode = track_feature['mode']
    key_mode = f"{key}-{mode}"

    key_mode_probabilities = key_mode_class_distribution[key_mode]
    key_mode_sorted_probabilities= sorted(key_mode_probabilities.items(), key=lambda x: x[1], reverse=True)
    key_mode_non_zero_probabilities = list(filter(lambda x: x[1] != 0.0, key_mode_sorted_probabilities))

    from random import uniform
    random_number = uniform(0, 100)
    cumulative = 0
    
    for key_mode, probability in key_mode_non_zero_probabilities:
        cumulative += probability
        if random_number <= cumulative:
            return key_mode

    