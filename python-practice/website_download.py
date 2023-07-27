import requests
import os
import webbrowser as wb

url = "https://example.com/"
response = requests.get(url)
print(type(response))
print(response.ok)
print(response.status_code)
print(response.reason)
print(response.text)

with open("example.html","w", encoding = response.encoding) as f:
    f.write(response.text)
file_path = os.path.realpath("example.html")
print(file_path)

wb.open("file://" + file_path)