import requests
import json
import http.client

conn = http.client.HTTPSConnection("api.themoviedb.org")
payload = "{}"
conn.request("GET", "/3/discover/movie?with_genres=35&primary_release_date.gte=2000&page=3&include_video=false&include_adult=false&sort_by=popularity.desc&language=en-US&api_key=3a899625a7cc0a7b39c1abcf69a1e28c", payload)

res = conn.getresponse()
data = res.read()
js = json.loads(data)
#print(data.decode("utf-8"))
#print(json.dumps(js, indent=4))
for i in range(20):
    id = js["results"][i]["id"]
    title = js["results"][i]["title"]
    print(id,title)
