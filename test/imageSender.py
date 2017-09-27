import requests

url = "http://localhost/imageOpener.py"
files = open('green_jay.jpeg', 'rb')

r = requests.post(url, data=files)
print r