import os

os.system(f"playerctl metadata >| {os.getenv('HOME')}/.config/dotfiles/_music.data")

with open(f"{os.getenv('HOME')}/.config/dotfiles/_music.data", "r") as f:
    data = f.read()

if data == '':
    print(" ♪ Nothing playing ♪ ")
else:
    name = ''
    artist = ''
    _data = data.split("\n")
    for item in _data:
        items = item.split("   ")
        if ":title" in items[0]:
            name = items[-1].strip()
        if ":artist" in items[0]:
            artist = items[-1].strip()
    if len(name) > 25:
        name = name[0:23] +'..'
    if len(artist) > 25:
        artist = artist[0:23] +'..'
    print(f"  ♪ {name} - {artist} ♪ ")
