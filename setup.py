import os
import sys

print("Checking if all required packages are installed..")
print("Please ensure you have i3-gaps and not i3..")

packages = [
    'i3',
    'i3blocks',
    'urxvt',
    'playerctl',
    'dunst',
    'nmcli',
    'rofi',
    'wal'
]

n = 0

for i in packages:
    if os.system(f'command -v {i}') != 0:
        print(f"{i} not found..")
        n += 1

assert n == 0, "Packages were found missing"

print("Creating necessary directories..")

paths = [
    '/.config',
    '/.config/dotfiles',
    '/.config/dotfiles/media',
    '/.config/dotfiles/scripts',
    '/.config/scripts/i3blocks',
    '/.config/scripts/i3'
    '/.config/i3',
    '/.config/i3blocks',
    '/.config/dotfiles/pages',
    '/.urxvt'
]

if input("WARNING: This would delete and replace all default config. Proceed: [y/N] ") != 'y':
    sys.exit(1)

for i in paths:
    os.system(f"mkdir -p $HOME/{i}")
    print(i)

files = [
    ('./i3/*', '/.config/i3/'),
    ('./i3blocks/*', '/.config/i3blocks/'),
    ('./media/*', '/.config/dotfiles/media/'),
    ('./urxvt/config', '/.config/.Xresources'),
    ('./urxvt/ext/*', '/.urxvt/'),
    ('./scripts/*', '/.config/dotfiles/scripts/'),
    ('./pages/*', '/.config/dotfiles/pages/')
]

for i in files:
    os.system(f'cp -r {i[0]} $HOME{i[1]}')
    print(i[0], i[1])

os.system(
    'xrdb merge ~/.config/.Xresources'
)
