import sys
import requests
import re
from create_directory import *
from download_image import *

url = "https://www.rokomari.com/book/publisher/3594/dimik-prokashoni"

response = requests.get(url)
if response.ok is False:
    sys.exit("Could not get response from server")

page_content = response.text

book_info = re.compile(r'<div class="book-list-wrapper ">\s*<a href="(.*?)"\s*title="(.*?)"[^>]*>.*?<div class="book-img">\s*<img src=".*?" data-src="(.*?)\s*alt')

result = re.findall(book_info,page_content)

folder_pattern = re.compile(r'book/(\d+)/(\w+)-(\w+)-')

if result:
    for item in result:
        print("Name : " + item[1])
        print("URL : https://www.rokomari.com" + item[0])
        print("Image : "+item[2])
        print("")

        match = re.findall(folder_pattern, item[0])
        print("Match = ",match[0])
        folder_name = "_".join(match[0])
        if folder_name:
            print(folder_name)
        else:
            print("No match")
        create_sub_directories(folder_name)
        download_image(item[2], folder_name)
else:
    print("No match")