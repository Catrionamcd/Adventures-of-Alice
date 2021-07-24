# A text base adventure game called Adventures of Alice
# Author : Catriona McDonnell


# Import google sheets as story content and flow are
# stored in a google sheet called Adventures-of-Alice
# Import story file which prints the story introduction
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

# Googlesheet with two pages, one for the story content
# and prompts. The other for the valid answers, possible
# outputs and the next step

STORY_PROMPT = SHEET.worksheet('AlicePrompt')
STORY_FLOW = SHEET.worksheet('AliceFlow')

all_prompts = STORY_PROMPT.get_all_values()
data_flow = STORY_FLOW.get_all_values()

# Data2 will be a global variable and will hold the
# data from the second page of the spreadsheet to
# ascertain the next step to take in the story
data2 = []


def game_start():
    """
    Start of game. This function is called from the main
    function. It will print the story intro which is
    imported form the story.py file. It will loop until
    a players name is entered. The player name will be
    returned to the main function.
    """
    story_intro()
    while True:
        print()
        player = input(
            "Enter your name here to start the adventure:\n").capitalize()
        if player == "":
            print("To play the game you must enter a name !!")
            continue
        else:
            break

    print(f"\nWelcome {player} to this world of adventure!")
    return player


def want_new_game():
    """
    This function is called in main function. Boolean value
    of False is returned if the player does not want to play
    again. If the player chooses Y, a boolean value of True
    is returned.
    The function will loop until a correct answer, Y or N
    is entered.
    """
    while True:
        play_again = input("Do you want to play again (Y/N)?\n").upper()
        if play_again != "Y" and play_again != "N":
            print("Invalid answer, please enter Y or N")
            continue
        if play_again == "Y":
            return True
        else:
            print("Thanks for playing, I hope you enjoyed it!")
            return False


def validate_player_input(curr_step):
    """
    This function is called from the main function. It accepts an
    input from the player in reponse to the story prompt. It validates
    the players input against the correct reponses from the second
    page of spreadsheet data - Alice Flow. It will return the item
    of data that corresponds to the valid input or it will return None.
    """
    player_response = input().upper()
    for item in data2:
        if item[0].isnumeric():
            if int(item[0]) == curr_step and player_response == item[1]:
                return item
        else:
            continue

    return None


def main():
    """
    This function runs all program functions. The current step will
    be initialised to 1 for the start of the story. The rows in the
    google sheet that have the value in the current step will be
    appended to a new array data2. This data will be validated
    Current step will be used to extract the story content and prompt
    from the first google sheet and appended to a new array and this
    will be printed and the player prompted for an answer.
    """
    win_count = 0
    lose_count = 0
    global data2

    player = game_start()

    while True:
        game_in_play = True
        curr_step = 1

        # Create a sublist data2 of the current step from data flow
        data2 = list(filter(lambda c: str(c[0])
                            == str(curr_step), data_flow))

        # Check if data exists in sublist, print error if not
        if len(data2) == 0:
            print(f"\nERROR: Data not found for Step {curr_step}")
            return

        while game_in_play:
            # Create sublist of story content & prompt of current step
            # to be printed to screen
            this_prompt = list(filter(lambda c: str(c[0])
                                      == str(curr_step), all_prompts))

            if len(this_prompt) != 1:
                print(f"\nERROR: Data prompt Step {curr_step}")
                return
            # Print story content and prompt to player
            print()
            print(this_prompt[0][1])

            # Run function to validate player input and return output
            # and next step for game
            item = validate_player_input(curr_step)
            if item is None:
                print("\n***** Invalid answer *****\n")
                continue
            else:
                if not item[2] == "":   # if output column not blank
                    print()
                    print(item[2])      # then print Output column
                if item[3] == "Win":
                    win_count += 1
                    print(f"\nCongratulations {player}, Order is restored.\n")
                    game_in_play = False
                elif item[3] == "Lose":
                    lose_count += 1
                    print(f"\nHard luck {player}, better luck next time\n")
                    game_in_play = False
                else:
                    curr_step = int(item[3])  # next step move to current step
                    data2 = list(filter(lambda c: str(c[0])
                                        == str(curr_step), data_flow))
                    if len(data2) == 0:
                        print(f"\nERROR: Data not found for Step {curr_step}")
                        return

        if win_count == 1:
            print(f"\n{player}, you have won {win_count} game so far!!")
        else:
            print(f"\n{player}, you have won {win_count} games so far!!")
        if lose_count == 1:
            print(f"You have lost {lose_count} game so far!!")
        else:
            print(f"You have lost {lose_count} games so far!!")

        if not want_new_game():
            break


# Running the main function
main()
