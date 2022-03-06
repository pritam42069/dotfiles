import os
import time

for i in os.listdir("./"):
    os.system(f"wal -i {i}")
    time.sleep(20)
