# Add Module
import requests
import json
import os
import platform
import time
from fake_useragent import UserAgent

def clear_screen():
    system_platform = platform.system()

    if system_platform == "Windows":
        command = "cls"
    elif system_platform == "Linux":
        command = "clear"
    else:
        command = "clear"
    os.system(command)

ua = UserAgent()
headers = {'User-Agent': ua.random}

menu = """\033[36m
▪   ▄▄▄·    .▄▄▄  ▄• ▄▌▄▄▄ .▄▄▄   ▄· ▄▌
██ ▐█ ▄█    ▐▀•▀█ █▪██▌▀▄.▀·▀▄ █·▐█▪██▌
▐█· ██▀·    █▌·.█▌█▌▐█▌▐▀▀▪▄▐▀▀▄ ▐█▌▐█▪
▐█▌▐█▪·•    ▐█▪▄█·▐█▄█▌▐█▄▄▌▐█•█▌ ▐█▀·.
▀▀▀.▀       ·▀▀█.  ▀▀▀  ▀▀▀ .▀  ▀  ▀ • 

1- Ip Query
2- Github
3- Exit
"""

def countdown(seconds):
    while seconds > 0:
        print(f"\033[33mTime remaining: {seconds} seconds\033[0m", end='\r')
        time.sleep(1)
        seconds -= 1

    print("\nCountdown complete!")

def ipİnfo():
    clear_screen()
    print(menu)
    ipaddress = input("Enter the any Ip Address: \033[0m")
    fields = [
        'status', 'continent', 'continentCode', 'country', 'countryCode',
        'region', 'regionName', 'city', 'district', 'zip', 'lat', 'lon',
        'timezone', 'isp', 'org', 'as', 'asname', 'reverse', 'mobile',
        'proxy', 'hosting', 'query'
    ]
    url = f"http://ip-api.com/json/{ipaddress}?fields={','.join(fields)}"

    response = requests.get(url, headers=headers) # Make Requests
    data = response.json()
    data['author'] = 'omicr0nn'
    file_name = ipaddress + ".json"

    if response.status_code == 200:
        print("\033[35mRequests successfully")
        try:
            # Create and Save File
            with open(file_name, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print(f"\033[32mThe file named {file_name} has been saved")
        except:
            print("\033[31mFile creation failed")
    else:
        print("\033[31mRequest failed")
    
    countdown(5)

while True:
    ipİnfo()