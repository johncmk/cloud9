import requests as req

url = 'https://jsonplaceholder.typicode.com/posts/1'
#url = 'http://www.naver.com'


serviceResponse = req.get(url, verify=False)

print serviceResponse.text