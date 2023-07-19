import json
import urllib.request

min_version = (3, 8, 0)

url = "https://raw.githubusercontent.com/actions/python-versions/main/versions-manifest.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

versions = []

for item in data:
    version_str = item["version"]
    version_tuple = tuple(map(int, version_str.split(".")))
    if version_tuple >= min_version:
        versions.append(version_str)

print(json.dumps(versions))
