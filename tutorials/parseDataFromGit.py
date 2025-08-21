from pathlib import Path
import requests
data_dir = Path('data'); data_dir.mkdir(exist_ok=True)  # Ensure the data directory exists
response = requests.get("https://api.github.com/repos/laravel/laravel")
response.raise_for_status()  # Ensure the request was successful
data = response.json()  # Parse the JSON response
# Save the data into a csv file
with open(data_dir / 'python_repo_test_data.csv','w') as file:
    file.write("name,stargazers_count,language\n")
    file.write(f"{data['name']},{data['stargazers_count']},{data['language']}\n")