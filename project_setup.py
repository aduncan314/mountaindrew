import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_settings():
    try:
        with open(os.path.join(BASE_DIR, 'config.json'), 'r') as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError("FATAL ERROR: configurations not properly set")
