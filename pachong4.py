import requests

# get请求
url = 'http://httpbin.org/get'
data = {
    "name": "chris",
    "age": 31
}
# .get是使用get方式请求url，字典类型的data不用进行额外处理
response = requests.get(url, data)
print(response.text)

url = 'http://httpbin.org/post'
response = requests.post(url, data)
print(response.json())

