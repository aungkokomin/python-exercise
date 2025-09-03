import json

import requests,csv
from pathlib import Path

def fetch_data_from_api(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        # Store data in a CSV file
        with open(Path("api_data.json"),"w") as jsonfile:
            json.dump(response.json(),jsonfile,indent=4)
    except(requests.RequestException, ValueError) as e:
        return f"Error fetching data: {e}"

if __name__=="__main__":
    dataUrl = "https://api.github.com/repos/python/cpython"
    fetch_data_from_api(dataUrl)