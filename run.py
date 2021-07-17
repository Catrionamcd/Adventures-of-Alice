# A text base adventure game called Adventures of Alice
# Author : Catriona McDonnell

import sys
import time
import linecache
import gspread
from google.oauth2.service_account import Credentials
from story import story_intro

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Adventures-of-Alice")

STORY_PROMPT = SHEET.worksheet('AlicePrompt')
STORY_FLOW = SHEET.worksheet('AliceFlow')

# curr_step = 1
# data1 = story.get_all_values()[curr_step]
# data2 = flow.get_all_values()[curr_step]

# print(data1[1])

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
    print(f"Welcome {player} to this world of adventure!")
    do_you_follow_rabbit()


# def read_storyline(line_num, num_of_lines):
#     """
#     Read the story text file to print just the section of the story
#     that is relevant
#     """
#     print(line_num)
#     print(num_of_lines)
#     print()
#     story_lines = (linecache.getlines('story.txt')[line_num:num_of_lines])
#     for line in story_lines:
#         line = line.strip()
#         print(line)

    
def do_you_follow_rabbit(): 
#     """
#     Player will have to chose to follow the white rabbit or not
#     by typing in yes or no.
#     """   
      curr_step = 1
      data1 = STORY_PROMPT.get_all_values()[curr_step]
      data2 = STORY_FLOW.get_all_values()[curr_step]

      print(data1[1]) 

#     line_num = 0
#     num_of_lines = 8
#     read_storyline(line_num, num_of_lines)

#     while True:
#         print()
#         follow_rabbit = input("Do you follow the white rabbit(Y/N)?\n").capitalize()
#         if follow_rabbit == "Y" or follow_rabbit == "N":
#             break
#         else:
#             print("You must answer 'Y' or 'N'?")
#             continue            

#     if follow_rabbit == "N":
#         print("Not following rabbit")
#     else:
#         hole_in_tree()


# def hole_in_tree():
#     """
#     Player and Alice fall through hole in the tree and land
#     in a strange room with three doors/three options.
#     """
#     line_num = 9
#     num_of_lines = 13
#     read_storyline(line_num, num_of_lines)
    
#     print()
#     door_choice = input("Which door should you choose(1, 2, 3)?\n")
#     if door_choice == 1:
#         print("Door 1")
#     elif door_choice == 2:
#         print("Door 2")
#     elif door_choice == 3:
#         print("Door 3")
#     else:
#         print("Invalid choice, you must enter 1, 2 or 3")
     
 
#
#  The game starts here by running game start function
#
game_start()
