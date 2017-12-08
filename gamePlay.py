from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://192.168.2.160:9000/api/training' # Set destination URL here
post_fields = {'key': 'ikb9qdsm', 'turns':1}     # Set POST fields here

request = Request(url, urlencode(post_fields).encode())

json = urlopen(request).read().decode()

#print(json)

#post_fields2 = {'key':'ikb9qdsm', 'turns':1 }
#request2 = Request(url, urlencode(post_fields).encode())

#json2 = urlopen(request).read().decode()

game = json['game']
id = game['id']
turn = game['turns']
maxTurns = game['maxTurns']
heroes = game['heroes']











