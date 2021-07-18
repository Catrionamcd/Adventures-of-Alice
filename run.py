# A text base adventure game called Adventures of Alice
# Author : Catriona McDonnell

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

data_flow = STORY_FLOW.get_all_values()

data2 = data_flow

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

    print(f"\nWelcome {player} to this world of adventure!")


def want_new_game():
    while True:
        play_again = input("Do you want to play again (Y/N)?\n").upper()
        if play_again != "Y" and play_again != "N":
            print("Invalid answer, please enter Y or N")
            continue
        
        if play_again == "Y":
            return True
        else:
            return False


def validate_player_input(curr_step):
    """
    Validates the players input against the correct reponses
    from spreadsheet data
    """
    player_response = input().upper()

    for item in data2:
        if item[0].isnumeric():
            if int(item[0]) == curr_step and player_response == item[1]:
                return item
        else:
            continue

    return None


#
#  The game starts here by running game start function
#
def main():
    """
    Run all progran functions.
    """
    win_count = 0
    lose_count = 0

    game_start()

    while True:
        game_in_play = True
        curr_step = 1
        
        # data2 = get-sublist(curr_step)
        data2 = list(filter(lambda c: str(c[0]) == str(curr_step), data_flow))
        if len(data2) == 0:
            print(f"\nERROR: Data not found for Step {curr_step}")
            return

        while game_in_play:
            # get_current_step(curr_step)
            all_prompts = STORY_PROMPT.get_all_values()
            this_prompt = list(filter(lambda c: str(c[0])
                                      == str(curr_step), all_prompts))
            if len(this_prompt) != 1:
                print(f"\nERROR: Data prompt Step {curr_step}")
                return
            print()
            print(this_prompt[0][1])
            
            item = validate_player_input(curr_step)
            if item == None:
                print("\n** Invalid answer **\n")
                continue
            else:
                if not item[2] == "":        # if output column not blank
                    print()
                    print(item[2])  # then print Output column
                if item[3] == "Win":
                    win_count += 1
                    print("\nCongratulations, you won. Order is restored.\n")
                    game_in_play = False
                elif item[3] == "Lose":
                    lose_count += 1
                    print("\nHard luck, better luck next time\n")
                    game_in_play = False
                else:
                    curr_step = int(item[3])
                    data2 = list(filter(lambda c: str(c[0]) 
                                        == str(curr_step), data_flow))
                    if len(data2) == 0:
                        print(f"\nERROR: Data not found for Step {curr_step}")
                        return

        if not want_new_game():
            break

        print(f"\nYou have won {win_count} games so far!!")
        print(f"You have lost {lose_count} games so far!!")


main()
