from urllib.request import Request, urlopen
import requests
import json

def get_ip():
    ip = "None"
    try:
        ip = urlopen(Request("https://ipinfo.io/ip")).read().decode().strip()
    except:
        pass
    
    return ip
    
def get_location():
    location = "None"
    try:
        r = json.loads(requests.get("https://ipinfo.io/json").text)
        location = str(r["city"] + " / " + r["region"])
    except:
        pass
    
    return location