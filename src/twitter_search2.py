

import requests
import json

endpoint = "https://api.twitter.com/1.1/tweets/search/30day/dev.json" 

headers = {"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAANyv9QAAAAAAaXjzEFP8n1itesKd%2BtvthzYMqSQ%3DBahXOX83ENauzf8acDc6fiiC0ZhiQPrnNPmzHvXTRa4VRyaYCk", "Content-Type": "application/json"}  

data = '{"query":"(snow OR sleet OR hail OR (freezing rain)) has:images", "fromDate": "201802020000", "toDate": "201802240000"}'

response = requests.post(endpoint,data=data,headers=headers).json()

print(response)

# headers = {"Authorization":"Bearer MYREALLYLONGTOKENBASEDONKEYS", "Content-Type": "application/json"}  