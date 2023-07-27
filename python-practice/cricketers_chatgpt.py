import re

with open("cricketers.html", "r") as fp:
    cricketers = fp.read()

pattern = r'<li>\s*(.*?)\s*<ol>(.*?)</ol>'
matches = re.findall(pattern, cricketers, re.DOTALL)

for match in matches:
    country = match[0].strip()

    players = re.findall(r'<li>(.*?)</li>',match[1], re.DOTALL)
    player_names = ", ".join(player.strip() for player in players)
    
    print(country ,"-", player_names)
