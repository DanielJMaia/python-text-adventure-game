# Main game file
from art import tprint
import os
from game_functions import get_player_name, start_adventure


os.system("clear")

# Calls get_player_name and returns the player name
def main():

    starting_health = 30
    
    get_player_name()

    start_adventure(starting_health)

    tprint("Game Over")

if __name__ == '__main__':
    main()