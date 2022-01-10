from pathlib import Path

# In Working

#Created at *.*.2021
#Last Update 10.01.2022

#Made by Neiki (Philipp Eckert)

#Private Github (https://github.com/EckertP)

def ask_file():
    while 1:
        path = Path(input(
            f"Enter the file name (example: pass.txt, wordlist.txt)\n>"))
        if not path.is_file():
            print('[!] No such file!')
            continue
        return path
