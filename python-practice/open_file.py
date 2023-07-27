import os
import webbrowser as wb

file_path = os.path.realpath("example.html")
print(file_path)
wb.open("file://" + file_path)