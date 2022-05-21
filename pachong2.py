from urllib import parse
from urllib import request
data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')
post = request.urlopen('http://httpbin.org/post', data=data)
print(post.read().decode('utf-8'))

get = request.urlopen('http://httpbin.org/get', timeout=1)
print(get.read())
