import socket
from clear_src import clear_src
from os import system

def banner(host):
    clear_src()
    system("title Banner Grabber")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        return print("Error")
    host = socket.gethostbyname(host)
    try:
        port = int(input("[!] Enter your Port to scan: "))
    except ValueError:
        return print("Input Port was not a Number!")
    try:
        s.connect((host, port))
        print("[!] Connection success!\nWaiting for the Banner....\n")
        if port == 80:
            msg = "HEAD / HTTP/1.0\r\n\r\n"
            msg = msg.encode()
            s.send(msg)
        data = s.recv(1024)
        print("Banner:\n"+data.decode())

        s.close()
    except Exception as Error:
        return print(Error)