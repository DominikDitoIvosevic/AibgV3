from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

url = 'http://192.168.3.251:9000/api/training' # Set destination URL here
post_fields = {'key': 'eyx3wvrg', 'turns':2, 'map': 'm1'}     # Set POST fields here
request = Request(url, urlencode(post_fields).encode())
jsonData = urlopen(request).read().decode()

print(jsonData)
jsonData = json.loads(jsonData)

playUrl = jsonData['playUrl']
post_fields2 = {'key':'ikb9qdsm', 'dir':'Stay' }
request2 = Request(playUrl, urlencode(post_fields2).encode())
json2 = urlopen(request2).read().decode()
print(json2)

json2 = json.loads(json2)


playUrl = json2['playUrl']
print(playUrl)
post_fields2 = {'key':'ikb9qdsm', 'dir':'Stay' }
request2 = Request(playUrl, urlencode(post_fields2).encode())
json3 = urlopen(request2).read().decode()
print(json3)

