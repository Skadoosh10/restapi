from urllib import request
import requests
#response = requests.get("https://api.thecatapi.com/v1/images/search")
#print(response.json())

url = "https://api.thecatapi.com/v1/images/search"
resp=requests.get(url=url)
print(resp.text)