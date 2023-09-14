
cricket_players = []

# Function to add a player's details
def add_player():
    player = {}
    player['Name'] = input("Enter player's name: ")
    player['Team'] = input("Enter player's team: ")
    player['Batting Average'] = float(input("Enter batting average: "))
    player['Bowling Average'] = float(input("Enter bowling average: "))
    cricket_players.append(player)

# Function to display all player details
def display_players():
    if not cricket_players:
        print("No player details available.")
    else:
        print("\nPlayer Details:")
        for idx, player in enumerate(cricket_players, start=1):
            print(f"Player {idx}:")
            for key, value in player.items():
                print(f"{key}: {value}")
            print()

# Main menu
while True:
    print("\nOptions:")
    print("1. Add a player")
    print("2. Display player details")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_player()
    elif choice == '2':
        display_players()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
    
# End of the program