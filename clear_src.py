import platform
from subprocess import call
operSys = platform.system()

def clear_src():
    if operSys == "Windows":
        call("cls", shell=True)
    if operSys == "Linux":
        call("clear", shell=True)