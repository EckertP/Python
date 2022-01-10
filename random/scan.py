import os
from datetime import datetime

def scan():
    list = os.listdir()
    scanstart = datetime
    for file in list:
        print(file)

    endtime = datetime

    print(f"Finished aftert {endtime - scanstart}")


try:
    scan()
except Exception as e:
    print(e)