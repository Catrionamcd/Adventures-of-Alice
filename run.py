# A text base adventure game called Adventures of Alice
# Author : Catriona McDonnell


"""
Introduction to the game and game name
"""
print()
print("**************************************************")
print()
print("Aventure game that brings you through a Wonderland")
print("with Alice. Meet fantastic creatures along the way")
print("and help restore balance to Wonderland by helping")
print("Alice to slay the Jabberwocky!")

print()
print("    ***************************************")
print("    *                                     *")
print("    *             Welcome to              *")
print("    *                the                  *")
print("    *         Adventures of Alice         *")
print("    *                                     *")
print("    *                                     *")
print("    ***************************************")


def game_start():
    """
    Start of game 
    """
    print()
    player = input("Enter your name here to start the adventure:\n")
    if player == "":
        print("To play the game you must enter a name !!")
    else:
        print(f"Welcome {player} to the world of Alice")

game_start()
    
    
