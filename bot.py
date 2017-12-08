from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://192.168.2.160:9000/api/training' # Set destination URL here
post_fields = {'key': 'ikb9qdsm', 'turns':1}     # Set POST fields here
request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)


post_fields2 = {'key':'ikb9qdsm', 'dir':'Stay' }
request2 = Request(url, urlencode(post_fields2).encode())
json2 = urlopen(request2).read().decode()
print(json2)


