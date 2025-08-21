from pathlib import Path
import requests
data_dir = Path('data'); data_dir.mkdir(exist_ok=True)  # Ensure the data directory exists
response = requests.get("https://api.github.com/repos/aungkokomin/lms_backend_api")
response.raise_for_status()  # Ensure the request was successful
data = response.json()  # Parse the JSON response
repos_file = data_dir / 'pythontestdata.json'
repos_file.write_text(str(data), encoding='utf-8')  # Save the JSON data to a file