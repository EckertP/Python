import requests
import os

#Made on the 10.01.2022 in Python3

#This is for School Eductation
#Simple Request and Data Response Reader

#Based on the Website https://tweeterid.com

#Made by Neiki (Philipp Eckert)
#Private and Personal Github (https://github.com/EckertP)

def main():
    os.system("Get Twitter IDs")
    os.system("cls")
    print("Type here your Twitter User Name(s)! You can use with or without the @")
    print("You can get up to 20 Ids at the same time! It will take some time but it works")
    print('Split the Names with ","! Without it will not work')
    name = input("> ")
    if not name:
        input("Wrong Input")
        main()
    if "," in name:
        name = name.split(",")    
        check = len(name)
        if check >= 21:
            input("Too much Users! Please be under 20 of one time")
            main()
        for n in name:
            if "@" in n:
                n = n.split("@")[1]
            r = requests.post("https://tweeterid.com/ajax.php", data= {
                'input': n
            })
            if r.text == 'error':
                print(f"[!] > Twitter ID for {n} not Found! (https://twitter.com/{name})")
            else:
                print(f"[*] > {n} twitter Id = {r.text}")
    else:
        if "@" in name:
            name = name.split("@")[1]
        r = requests.post("https://tweeterid.com/ajax.php", data= {
                'input': name
        }) 
        if r.text == 'error':
            print(f"[!] > Twitter ID for {name} not Found! (https://twitter.com/{name})")
        else:
            print(f"[*] > {name} twitter Id = {r.text}")
    input("FINISHED! Press any key to exit")
    exit(code="Exit")
try:
    main()
except Exception as E:
    input(E)