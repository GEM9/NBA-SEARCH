import requests  # Import requests
import json
from prettytable import PrettyTable

# RapidAPI key
RAPIDAPI_KEY = "c15875bd39mshd4bb1e52889c2f6p1ce620jsn6d371beecf72"


def get_player(player_id):
    url = f"https://free-nba.p.rapidapi.com/players/{player_id}"  # Corrected the URL

    headers = {
        'X-RapidAPI-Key': RAPIDAPI_KEY,
        'X-RapidAPI-Host': "free-nba.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)  # Using requests.get to make the HTTP GET request
    return response.json()  # Return the JSON response


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


def menu():
    while True:
        print("1. Search a specific player")
        print("2. Search a specific team")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            player_id = input("Enter the player ID: ")
            player_data = get_player(player_id)
            display_player(player_data)
        elif choice == '2':
            team_id = get_team()
            diplay_team(team_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")


menu()
