# A text base adventure game called Adventures of Alice
# Author : Catriona McDonnell

import time
import linecache
from story import story_intro


def game_start():
    """
    Start of game 
    """
    story_intro()
    while True:
        print()
        player = input("Enter your name here to start the adventure:\n").capitalize()
        if player == "":
            print("To play the game you must enter a name !!")
            continue
        else:
            break
    print()
    print(f"Welcome {player} to the world of the Adventures of Alice!")

game_start()

def read_storyline(line_num, num_of_lines):
    """
    Read the story text file to print just the section of the story
    that is relevant
    """
    print()
    story_lines = (linecache.getlines('story.txt')[line_num:num_of_lines])
    for line in story_lines:
        line = line.strip()
        print(line)
    
def do_you_follow_rabbit(): 
    """
    Player will have to chose to follow the white rabbit or not
    by typing in yes or no.
    """   
    line_num = 0
    num_of_lines = 7
    read_storyline(line_num, num_of_lines)

    while True:
        follow_rabbit = input("Do you follow the white rabbit(y/n)?\n").capitalize()
        if follow_rabbit == "Y" or follow_rabbit == "N":
            break
        else:
            print("You must answer 'Y' or 'N'?")
            continue            

    if follow_rabbit == "N":
        print("Not following rabbit")
    else:
        print("Following rabbit")
    

do_you_follow_rabbit()
