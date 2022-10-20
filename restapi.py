from urllib import request
import requests

url = "https://api.thecatapi.com/v1/images/search"
resp=requests.get(url=url)
print(resp.text)
