import requests
import os

def download_csv(link, fname):

    with requests.get(link) as r:
        t = r.text

    with open(os.path.join('original_data', fname), 'w') as f:
        f.write(t)
    