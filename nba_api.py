import requests  
import json
from prettytable import PrettyTable

# RapidAPI key
RAPIDAPI_KEY = "c15875bd39mshd4bb1e52889c2f6p1ce620jsn6d371beecf72"


# GET A PLAYER
def get_player(player_id):
    url = f"https://free-nba.p.rapidapi.com/players/{player_id}"  # Corrected the URL

    headers = {
        'X-RapidAPI-Key': RAPIDAPI_KEY,
        'X-RapidAPI-Host': "free-nba.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)  # Using requests.get to make the HTTP GET request
    return response.json()  # Return the JSON response

# PLAYER DATA TABLE
def display_player(player_data):
    table = PrettyTable()
    table.field_names = [
        "ID", "First Name", "Last Name", "Position", "Team",
        "Height (feet)", "Height (inches)", "Weight (pounds)"
    ]
    table.add_row([
        player_data['id'],
        player_data['first_name'],
        player_data['last_name'],
        player_data['position'],
        player_data['team']['full_name'],
        player_data['height_feet'],
        player_data['height_inches'],
        player_data['weight_pounds']
    ])
    print(table)


# GET A TEAM 
def get_team(team_id):
    url = f"https://free-nba.p.rapidapi.com/teams/{team_id}"

    headers = {
        'X-RapidAPI-Key': RAPIDAPI_KEY,
        'X-RapidAPI-Host': "free-nba.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return response.json()

# TEAM DATA TABLE
def display_team(team_data):
    table = PrettyTable()
    table.field_names = ["ID", "Abbreviation", "City", "Conference", "Division", "Full Name"]
    table.add_row([
        team_data['id'],
        team_data['abbreviation'],
        team_data['city'],
        team_data['conference'],
        team_data['division'],
        team_data['full_name']
    ])
    print(table)

