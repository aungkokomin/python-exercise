import requests, pathlib
response = requests.get("https://api.github.com/repos/python/cpython")
response.raise_for_status()  # Ensure the request was successful
info = response.json()  # Parse the JSON response

print(info['stargazers_count'])  # Read and print the JSON from the file