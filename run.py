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
    curr_step = 1
    get_current_step(curr_step)

  
def get_current_step(curr_step): 
    """
    Gets the current step of the game 
    """   
    text_prompt = STORY_PROMPT.get_all_values()[curr_step]
    print(text_prompt[1]) 

    #response = input()

    validate_player_input(curr_step)

    
def validate_player_input(curr_step):
    """
    Validates the players input against the correct reponses
    from spreadsheet data
    """

    player_response = input()

    data2 = STORY_FLOW.get_all_values()

    valid_response_list = []

    for item in data2:
        if item[0].isnumeric():
            item[0] = int(item[0])
        else:
            continue

        if item[0] == curr_step:
            valid_response_list.append(item[1])
    
    valid_reponse = False
    for item in valid_response_list:
        print(item)
        if player_response == item:
            valid_reponse = True
            break
        
    if not valid_reponse:    
        print(f"Invalid answer, you must enter {valid_response_list}")     
        
    
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
