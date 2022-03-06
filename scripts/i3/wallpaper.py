import random
import os

wallpapers = os.listdir(f"{os.getenv('HOME')}/.config/dotfiles/media/backgrounds")

print(random.choice(wallpapers))