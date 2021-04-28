# Python Text RPG
# Alien Breach
# By Trenton Nelms

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100





#### Player Setup #### 
class player: 
	def __init__(self):
		self.name = ''
		self.hp = 0
		self.location = 'start_location'
myPlayer = player()

#### Title Screen #### 
def title_screen_selections():
	option = input("> ")
	if option.lower() == ("play"):
		start_game() #placeholder until we create it. #

	elif option.lower() == ("help"):
		help_menu() #another placeholder
	elif option.lower() == ("quit"):
		sys.exit()
	while option.lower() not in ['play', 'help', 'quit']:
		print("Please enter a valid command.")
		option = input("> ")
		option = input("> ")
		if option.lower() == ("play"):
			start_game() #placeholder until we create it. #

		elif option.lower() == ("help"):
			help_menu() #another placeholder
		elif option.lower() == ("quit"):
			sys.exit()

def title_screen():
	#Clears the terminal of prior code for a properly formatted title screen.
	os.system('clear')
	#Prints the pretty title.
	print('#' * 45)
	print('#          A L I E N | B R E A C H          #')
	print("#              Trenton Nelms                #")
	print('#' * 45)
	print("                 .: Play :.                  ")
	print("                 .: Help :.                  ")
	print("                 .: Quit :.                  ")
	title_screen_options()


def help_menu():
	print("###########################")
	print("# A L I E N | B R E A C H #")
	print("###########################")
	print('-Use up, down, left, right to move.')
	print('-Type your commands to do them.')
	print('-Use "look" to inspect something.')
	print('-Use "touch" to interact with something.')
	print('-Good luck and have fun!')
	title_screen_selections()



#### Map ####

"""
							 ======================================
							 #									  #
							 #									  #
							 #									  #
							 #			   BARRACKS				  #
							 #									  #
							 #									  #
							 ======================================
							 ___________	|     |   __________
							|			|	|     |  |  SPACE   |
							|	ARMORY	|   |     |  |  SUIT'S  |
							|___________|	|     |  |__________| 
								|	|		|     |     |   |
								|	|		|     |     |   |
							 ======================================
			 ___________	 #									  #       __________
			|			|	 #									  #      |          |
		 	|ELECTRICAL |----#									  # -----|   MESS   |
			|   ROOM	|	 #			   BRIDGE				  #      |   HALL   |
			|			|----#									  # -----|          |
			|___________|	 #									  #      |__________|
							 ======================================
								|	|		|     |     |   |
								|   |		|     |     |   |
							  ---------		|     |   ----------    
							 | STORAGE |	|     |  |LABORATORY|
							 |	ROOOM  |	|     |  |          |
							  ---------		|     |   ---------- 
							 ======================================
							 #									  #
							 #									  #
							 #									  #
							 #			   ESCAPE POD			  #
							 #									  #
							 #									  #
							 ======================================

"""


ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'rigt', 'east'

solved_spaces = {'a1': False, 'b1': False, 'c1': False,
				 'a2': False, 'b2': False, 'c2': False,
				 'a3': False, 'b3': False, 'c3': False,
				 'a4': False, 'b4': False, 'c4': False,
				 'a5': False, 'b5': False, 'c5': False,
				 'a6': False, 'b6': False, 'c6': False,
				 'a7': False, 'b7': False, 'c7': False,
				 'a8': False, 'b8': False, 'c8': False,
				 'a9': False, 'b9': False, 'c9': False,}
zonemap = {
	'a1': {
		ZONENAME: "Barrack Entrance",
		DESCRIPTION: "description",
		EXAMINATION: "This place is torn to shreds. It smells of decay.",
		SOLVED: False,
		UP: 'up', 'north'
		DOWN: 'down', 'south'
		LEFT: 'left', 'west'
		RIGHT: 'rigt', 'east'


	}

}



#### Game Interactivity ####
def print_location():
	 print('\n' + ('#' *(4 + len(myPlayer.location))))
	 print('# ' + myPlayer.location.upper() + ' #')
	 print('# ' + zonemap[myPlayer.position][DESCRIPTION])
	 print('\n' + ('#' *(4 + len(myPlayer.location))))


##### Game Functions ####
def start_game():
	return



