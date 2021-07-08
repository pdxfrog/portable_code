"""Helper functions for dealing with  metadata"""

import json


def load_meta(meta_file):
    with open(meta_file, 'r') as f:
        metadata = json.loads(f.read())
    return metadata
