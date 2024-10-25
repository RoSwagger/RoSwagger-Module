# Made by RoSwagger Developers at roswagger.com
# Visit our creator program here for unrestricted access for free at
# discord.roswagger.com

import requests
import time

def Swagger(endpoint, username):
    while True:
        response = requests.get(f"https://roswagger.com/get/{endpoint}/{username}")
        CoolSwag = response.json()
        
        if "error" in CoolSwag and "Please wait" in CoolSwag["error"]:
            wait_time = CoolSwag.get("timeLeft", 5)
            print(f"Rate limit hit. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            return CoolSwag

def all(username): return Swagger('all', username)
def userId(username): return Swagger('userId', username)
def lastOnline(username): return Swagger('lastOnline', username)
def creationDate(username): return Swagger('creationDate', username)
def thumbnail(username): return Swagger('thumbnail', username)
def rap(username): return Swagger('rap', username)
def verified(username): return Swagger('verified', username)
def pastUsernames(username): return Swagger('pastUsernames', username)
