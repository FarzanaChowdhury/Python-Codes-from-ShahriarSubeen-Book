import requests
import os

def download_image(img_url, name):
    download_directory = os.path.join("Projects", "CollectInfoFromWebpage", "dimik_pub")
    file_name = os.path.join(download_directory, "name.jpg")

    print("Downloading", img_url)
    r = requests.get(img_url)

    with open(file_name, "wb") as file:
        file.write(r.content)