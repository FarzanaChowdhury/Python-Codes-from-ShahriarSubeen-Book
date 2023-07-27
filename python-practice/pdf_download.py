import requests
import os
import webbrowser as wb

base_url = "https://drive.google.com/file/d/1inGBCmTKCQTGgF_avKG1QBKZekOBq4nA/view"

# info_dt = {"name":"Subeen", "email": "book@subeen.com", "country":"Bangladesh"}

url = base_url + "process.php"

response = requests.post(url)

if response.ok is False:
    print("Error downloading the file")

with open("AIbook.pdf", "wb") as fp:
    fp.write(response.content)

print("download complete!")