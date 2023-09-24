# nba_api.py

import http.client
import random
import json

# RapidAPI key
RAPIDAPI_KEY = "c15875bd39mshd4bb1e52889c2f6p1ce620jsn6d371beecf72"

def get_random_player():
    conn = http.client.HTTPSConnection("free-nba.p.rapidapi.com")
    
    headers = {
        'X-RapidAPI-Key': RAPIDAPI_KEY,
        'X-RapidAPI-Host': "free-nba.p.rapidapi.com"
    }
    
    random_player_id = random.randint(1, 500)  # Get a random player
    
    conn.request("GET", f"/players/{random_player_id}", headers=headers)
    
    res = conn.getresponse()
    data = res.read()
    
    return data.decode("utf-8")
