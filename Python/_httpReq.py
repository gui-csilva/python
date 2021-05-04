import requests
import json

url = "https://futdb.app/api/clubs"
apiKey = "0410a41b-9357-420b-aa95-0d4c1d77062d"
_headers = {"X-AUTH-TOKEN": apiKey}
_params = {"page": 1, "limit": 30}
x = requests.get(url, headers = _headers, params = _params)
xDict = x.json()

for value in xDict["items"]:
    print(value["name"])
