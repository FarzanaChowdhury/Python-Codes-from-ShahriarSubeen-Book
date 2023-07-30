import requests
import webbrowser as wb 
import os

img_url = "https://i.pinimg.com/564x/4d/d1/c2/4dd1c211df75974b405647d483caeed0.jpg"

r = requests.get(img_url)

with open("tighnari.png","wb") as f:
    f.write(r.content)

# r.text => string object
# r.content => object of bytes class

# open the file
# file_path = os.path.realpath("tighnari.png")
# print(file_path)
# wb.open("file://" + file_path)


image_url2 = "https://ds.rokomari.store/rokomari110/ProductNew20190903/130X186/354f11421_112234.jpg"
r=requests.get(image_url2)

dir = os.path.join("Projects", "CollectInfoFromWebpage", "dimik_pub")
file_name = os.path.join(dir, "Boi.jpg")
with open(file_name, "wb") as fp:
    fp.write(r.content)

file_path = os.path.realpath("Boi.png")
print(file_path)
wb.open("file://" + file_path)
