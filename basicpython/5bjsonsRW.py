import json, pathlib
payload = {"app":"demo","version":"1.0.0"}
pathlib.Path("data/app.json").write_text(json.dumps(payload, indent=4)) # write JSON to file
loaded = pathlib.Path("data/app.json").read_text()
print(loaded)  # read JSON from file