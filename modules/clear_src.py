import platform
from subprocess import call
operSys = platform.system()

# In Working

#Created at *.*.2021
#Last Update 10.01.2022

#Made by Neiki (Philipp Eckert)

#Private Github (https://github.com/EckertP)

def clear_src():
    if operSys == "Windows":
        call("cls", shell=True)
    if operSys == "Linux":
        call("clear", shell=True)