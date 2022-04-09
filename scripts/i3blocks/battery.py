import psutil
import time

while True:
    battery = psutil.sensors_battery()
    print(round(battery.percent), "%", sep="")
    time.sleep(10)
