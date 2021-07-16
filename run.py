# A text base adventure game called Adventures of Alice
# Author : Catriona McDonnell

import time
from story import story_intro


def game_start():
    """
    Start of game 
    """
    story_intro()
    while True:
        print()
        player = input("Enter your name here to start the adventure:\n")
        if player == "":
            print("To play the game you must enter a name !!")
            continue
        else:
            break
    print()
    print(f"Welcome {player} to the world of the Adventures of Alice!")

game_start()

def read_storyline():
    """
    Read the story text file to print just the section of the story
    that is relevant
    """
    print()
    story_file = open("story.txt")
    story_lines = story_file.read()
    story_file.close()
    print(story_lines)

def follow_rabbit(): 
    """
    Player will have to chose to follow the white rabbit or not
    by typing in yes or no.
    """   
    read_storyline()

follow_rabbit()
