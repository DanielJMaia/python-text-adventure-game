# Functions relating to the game's functionaltiy
from image_functions import print_dungeon
from art import tprint
import os


namefile = "text_files/namefile.txt"

def get_player_name():
    """The player enters their name and gets assigned a variable called 'name'"""
    
    name = input("Welcome adventurer, what is your name?\n")
    alt_name="Steve"
    answer = input("Your name is " + name + ". Is that correct? Y/n\n")

    if answer.lower() in ["y", "yes"]:
        print("\nPleasure to meet you " + name.title() + ", let us begin our adventure!\n")
        print("----------------------------------------------------------------\n")
        with open(namefile, "w") as file_object:
            file_object.write(name)

    elif answer.lower() in ["n", "no"]:
        name = alt_name
        print("Seems like you might have hit your head walking in here! I'll just call you Steve. Nice to meet you Steve. Let's begin!")
        print("----------------------------------------------------------------\n")
        with open(namefile, "w") as file_object:
            file_object.write(name)

    else:
        name = "bla"
        print("That's not even a real answer! You think this is a joke? You know what, you don't get a name. You're going to be called bla. Let's begin!")
        print("----------------------------------------------------------------\n")
        with open(namefile, "w") as file_object:
            file_object.write(name)

def you_died(why):
    """The death function, takes one argument to explain why the player died"""
    print(why)
    tprint("Game Over")
    try:
        os.remove("text_files/namefile.txt")
    except FileNotFoundError:
        pass
    exit(0)

def start_adventure(starting_health):
    """Starts the adventure by showing the room image and printing out the first choice"""
    with open(namefile) as file_object:
        name = file_object.read()

    print("Freezing chills shoot down your spine as you jolt awake. You look around, the vague memory of what feels like a dream already fading away.")
    print("You can barely see around you. A meekly flickering torch is the only source of light in this large room. The darkness gnaws at your mind. You feel like you've been here before.")
    print("Finally, you find a doorway. It won't open, but there's a keyhole with a key in it. As you turn the key your mind is flooded with whispering sounds, thousands of voices telling you to stop, to stay with them.")
    print("'sssttttaaayyy wiiiitttthhhh usss " + name.title() + ".....staaayyy.")
    response = input("\nDo you LEAVE the room or do you STAY?\n")
    if response.lower() in ["stay", "s"]:
        you_died("\nYou scream and let go of the key. You try to jump backwards but your feet are stuck. As you start to sink into the stone floor, you see a shadowy figure materialize in front of you. 'Welcommeeeee' it says. 'You'll make a fine addition to my collectionnnn'")
    else:
        print("\nYou fling the door open and leap out of the room, shadowy hands grasping as your heels.\n")
        two_door_room(starting_health)

def two_door_room(starting_health):
    print_dungeon()
    response = input("You walk into a room with two doors at the end of it. Looking around there doesn't seem to be much more in the room. Do you STAY and look around, go through the door on the RIGHT or the door on the LEFT?")
    if response.lower == "stay":
        print("You rummage around the room a little more, and find a small hole in the wall. You reach inside and pull out a small potion. You")


    