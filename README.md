# Adventures of Alice

The Adventures of Alice is a text based adventure game. The game is based on the story of 'Alice's Adventures in Wonderland' and 'Through the Looking glass' by Lewis Carroll. The player is taken through a land of wonder and meets many fantastic creatures along the way. The aim of the game is to find the Vorpal sword and slay the Jabberwocky, a fierce dragon-like creature, who along with the Queen of Hearts has control over Wonderland. There is a short introduction to the game and the player is asked to enter their name. The player is asked a series of questions. Depending on how they answer these questions they will go through a series of different adventures and may or may not slay the Jabberwocky and restore order to Wonderland.

## Multi Screen mock-up of the game
![alt text](assets/images/Adventures-MultiScreen.png)
![alt text](assets/images/Adventures-Screen1.png)

## Design of the game
### Flowchart
![alt text](assets/images/Adventures-Flowchart.png)

## Features/Functions
### Existing Features

* The player is presented with a screen that gives an introduction to the game
and they are asked to enter their name to start their adventure. If a name is not entered a message will be displayed to inform the player that to play the game they must enter a name. This function will continue to loop until a players name is entered.

![alt text](assets/images/NameError-Screen.png)

* If a players name is entered, the capitalize() method is used to format the name entered and it is printed in a welcome statement. 
* The first step in the story begins. The player is presented with an option to follow the white rabbit. The function will get all values from the google sheets data.
* It will create a sublist of the values needed to validate the input from the player.
* It will return the output for the current step and the value ofthe next the next step.

![alt text](assets/images/Adventures-Screen2.png)

* If the players input response does not exist as a valid response for the current step in the game, an error message will be displayed and the player will have to enter the correct response to continue.

![alt text](assets/images/Adventures-Screen3.png)

* In the current data model there are seven ways to lose the game and two different ways to win. This is configurable.
* A tally of the players wins and losses is accumulated and displayed to the player at the end of each game.
* The player is also given the option to play again.

This shows one of the possible wins.

![alt text](assets/images/Adventures-Screen4.png)

This shows one of the possibe losses.

![alt text](assets/images/Adventures-Screen5.png)

* There is functionality to validate the data in the google sheets data structure. For example, if a next step is missing in the google sheets, the program  will output an error to alert the user that the data is missing and the data model is compromised.


![alt text](assets/images/Data-Error-Screen.png)

### Use of Python 

While coding this game I intially used a for loop to loop through the list of data that had been retreived from the google sheets. This loop would create a sublist of the data that was needed for validation and to get the next step. Using google I discovered a more powerful pythonic way of doing this in just one line. These are screen shots of my code as I had it before putting in the lambda function.

![alt text](assets/images/Code-with-loop.png)

These are the two websites I read to achieve this goal :

https://www.pythontutorial.net/python-basics/python-filter-list/

https://www.analyticsvidhya.com/blog/2020/03/what-are-lambda-functions-in-python/


### Future Features 
* The game could be extended to hold numerous stories. The player could be presented with a menu of different adventures to play. The google sheets could be extended to hold a story name column.
* An extra sheet could be updated to store the players name and tally of wins/losses.
* The game could have more options and extra scenarios to make it more interesting and complex. More characters from the original story, such as Tweedledee and Tweedledum could have been added.
* Art, maybe ASCII art, could be used to display the many iconic symbols associated with Alice in Wonderland, such as: a potions bottle, a drink me or eat me label or the Mad Hatters top hat perhaps.


## Data Model

This game uses Google sheets to store all the data for the game. The Adventures-of-Alice spreadsheet is comprised of two sheets. The AlicePrompt sheet stores two values, Step and User Prompt. The value in Step is numeric and represents where the player is in the game. The User Prompt holds the story content as well as the question the play is asked to respond to. This is printed to the screen.

![alt text](assets/images/Google-Sheet1.png)

The second sheet, AliceFlow, also stores the Step. The Step values should correspond to the values stored in the Step field in AlicePrompt. It also holds Response, which holds all the possible valid answers that the player may enter for the step that they are at in the game. The next value stored is Output, which will hold the possible outcomes based on the response the player enters. And finally, AliceFlow sheet stores the next step of the game also based on the players response.

![alt text](assets/images/Google-Sheet2.png)

The next step can be a numeric value but can also hold a Win or Lose value, which will end the game. The link for a copy of the Adventures Of Alice google sheets is here:
https://docs.google.com/spreadsheets/d/1bUZLqS3Y8-wCncuKFJdtRpnGloQ8lo0SaEltfV9jUIk/edit?usp=sharing

### Development of Data Model

When I first approached this project and decided to do a text based adventure game, I wanted the text and story content to be separate from my Python code. I wanted my program to open, read and manipulate the data rather than be hard coded into my program.

I experimented by using a text file, called story.txt in my gitpod repository. I initially used the open file, readlines, close file code in my program but then after some research I discovered the linecache.getlines() method and used this to read certain lines from the text file depending on where the player was in the story by using parameters of the file name and line number. The code is below:

![alt text](assets/images/LineCache-Code.png)

After reviewing the Love Sandwiches mini project, I felt it may be better to used Google Sheets to store the story line and content. I also realised that  I could also use it to store the valid answers to each player prompt, the output and the next step of the game. Hence, I discarded my original idea of using a text file to store and read in the relevant lines and used Google Sheets instead.
## Technology
### Language Used

* [Python](https://www.python.org) - Python is an interpreted high-level general-purpose programming language. I used Python to access the data in Google Sheets and run the game.

### Other Technologies and Libraries

* [GitPod](https://gitpod.io) - Gitpod is an online cloud based IDE. I developed and tested my project using Gitpod. I added and commited changes with messages and pushed to GitHub.
* [GitHub](https://github.com) - GitHub is a provider of Internet hosting for software development and version control using Git.
* [Heroku](https://heroku.com) - Heroku is a cloud platform as a service supporting several programming languages. I used Heroku to deploy and run the project.
* [Google Chrome Browser](https://www.google.com/intl/en_ie/chrome/) - was used to view the game.
* [Google Sheets](https://www.google.com/sheets/about/) - used to store the story flow, the story content, story prompts and the next steps for the game. 
* [Diagrams](https://wwww.diagrams.net) - used to create the flowchart for the project.

## Testing

PEP8 online check
http://pep8online.com
![alt text](assets/images/PEP8-Checker.png)

* No errors were found in the code 
### Manual Testing


## Deployment
Deployment
The application uses Heroku for deployement

To create the application:
First create the requirements file the Heroku will use to import the dependencies required for deployment: type pip3 freeze > requirements.txt. 

Navigate to the Heroku website
create an account by entering your email address and a password
Activate the account through the authentication email sent to your email account
Click the new button and select create a new app from the dropdown menu
Enter a name for the application which must be unique, in this case the app name is after-the-party
Select a region, in this case Europe
Click create app
Heroku settings
From the horizontal menu bar select 'Settings'.
In the buildpacks section, where further necessary dependencies are installed, click 'add buildpack'. Select 'Python' first and click 'save changes'. Next click 'node.js' and then click 'save changes' again. The 'Python' buildpack must be above the 'node.js' buildpack'. They can be clicked on and dragged to change the order if necessary.
Deployment
In the top menu bar select 'Deploy'.
In the 'Deployment method' section select 'Github' and click the connect to Github button to confirm.
In the 'search' box enter the Github repository name for the project. Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository which in this case is Adventures of Alice.
Scroll down to select either automatic or manual deployment. For this project automatic deployment was selected. If you wish to select automatic deployment select the button 'Enable Automatic Deploys'. This will rebuild the app every time a change is pushed to Github. If you wish to manually deploy click the button 'Deploy Branch'. The default 'Master' option in the dropdown menu should be selected in both cases.
When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser. The live deployment of the project can be seen here
The app starts automatically and can be restarted by pressing the 'Run Program' button.

Forking the Repository
If you wish to fork the repository to make changes without affecting the original you can fork the repository

Navigate to the adventures-of-alice repository
Click the 'Fork' button at the top right of the page.
A forked copy of the repository will appear in your Repositories page.
Cloning the Repository
On GitHub navigate to the main page of the repository.
Above the list of files click the dropdown code menu.
Select the https option and copy the link.
Open the terminal.
Change the current working directory to the desired destination location.
Type the git clone command with the copied URL: git clone https://github.com/catrionamcd/adventures-of-alice.git.

Press enter to create the local clone.

## Credits

* Adventures of Alice in Wonderland by Lewis Carroll
* Through the looking glass by Lewis Carroll
* Disney movies - Alice in Wonderland 1951 & 2010
               




