import os

with open("countries.html", "r") as fp:
    for country in fp:
        # char to ASCII value => ord()
        letter = ord(country[0]) + 32
        
        # ASCII to char => chr()
        new_file = chr(letter) + ".txt"
        with open(new_file,"a") as f:
            f.write(country +"\n")