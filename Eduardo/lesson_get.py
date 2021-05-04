import requests
import json

url = "https://futdb.app/api/clubs"

_headers = {"X-AUTH-TOKEN":"ca379bac-5fcd-4e13-b08c-03982189b0fb"}
_params = { "page":"1",
			"limit":"20"}

x = requests.get(url, headers=_headers, params=_params)

jsonResposta = x.json()
print(type(jsonResposta))
print(jsonResposta)