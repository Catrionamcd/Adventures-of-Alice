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

    validate_player_input(curr_step)

    
def validate_player_input(curr_step):
    """
    Validates the players input against the correct reponses
    from spreadsheet data
    """

    player_response = input().upper()

    data2 = STORY_FLOW.get_all_values()
    print(data2)

    valid_response = False
        
    for item in data2:
        if item[0].isnumeric():
            item[0] = int(item[0])
            if item[0] == curr_step and player_response == item[1]:
                curr_step = item[3]
                valid_response = True
                print(item[3])
                break
        else:
            continue

    

    #     if item[0] == curr_step:
    #         valid_response_list.append(item[1])
    
    # valid_reponse = False
    # for item in valid_response_list:
    #     if player_response == item:
    #         valid_reponse = True
    #         break

    if not valid_response:    
        print(f"Invalid answer, you must enter")     
        
    
#
#  The game starts here by running game start function
#
game_start()
