from nba_api import get_player, display_player, get_team, display_team


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
            team_id = input("Enter the team ID: ")
            team_data = get_team(team_id)
            display_team(team_data)
            
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

menu()
