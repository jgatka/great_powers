# Console app to assign players to great powers for the board game DIPLOMACY
# This code is functional and pragmatic...there's a reason I don't work in the development dept.
# Josh Gatka

# Import libraries
import random
from random import shuffle
import foo.insecure

# to do list
'''
TODO Need to insert a 'Board number x' statement in between board assignments. This will require a board count variable as well as a current board variable.
'''

# Declare variable for the number of players and set it equal to zero
# full path to the file containing the names of players, you will need to configure this
player_names_source_txt = ''
# generic press any key message string
press_any_key = "Press any key to continue..."
# the number of players that will need to be assigned to a board and a great power
player_count = 0
# The list of all of the great powers in DIPLOMACY
great_powers = ['Austria-Hungary', 'France', 'Germany', 'Great Britain', 'Italy', 'Russia', 'Turkey']
# create a list for all of the player names
player_names = []
current_board = 0
# The number of players that have been assigned a board and a great power
# This variable is used inside of the big assigning loop
num_assigned_players = 0
# Horizontal line for separating boards
horizontal_rule = '*______________________________________________________________________________*\n'

# Declare functions

# Function to check the number of players and return a message:
def check_player_count(player_count):
	# Check that there are at least 2 players
	if player_count < 2:
		print('You need at least 2 players!')
	# Check that there are no boards with only one player
	elif player_count % 7 == 1:
		print('\nYou need at least 1 more player.  Otherwise one of the boards will have only 1 player. :(\n ')
	# Otherwise, you're good to go, confirm number of players
	else:
		print('Ok, so %r players!') % player_count

# Calculate the number of boards that will have 7 players (full board)
def num_full_boards(player_count):
	num_full_boards = (player_count / 7)
	return num_full_boards

# calcuate the number of boards that will be needed which will not have a full table of 7 players
def incomplete_boards(player_count):
	if player_count % 7 > 0:
		return 1
	else:
		return 0

# Calculate the number of players who will be playing on a board that does not have 7 players
# These players will be playing a variation of the rules, where they control multiple great powers
def incomplete_board_players(player_count):
	num_extra_players = (player_count % 7)
	return num_extra_players

# function to get player names from a text file
def get_player_names_from_txt(names_text_file):
	r = open(names_text_file, 'r')
	for line in r:
		player_names.append(line.strip())
		player_count = len(player_names)
	print('\nThere are %r players.\nThere will be %r full board(s), each with 7 players.\nThere will be %r incomplete board(s), with %r players\n'  % (player_count, num_full_boards(player_count), incomplete_boards(player_count), incomplete_board_players(player_count)))
	r.close
	raw_input(press_any_key)

''' 
# Below is the old logic, which required that users manually enter the number of players and their names.
	
# User inputs number of players, if number is less than 3 they will be forced to choose again
while player_count < 2 or player_count % 7 == 1:
	player_count =int(raw_input("How many players?\n>"))
	# Check that there are at least three players, and that there are no boards with only one player
	check_player_count(player_count)

# Get player names, add them to a list
current_player = 1
while current_player <=1 or current_player <= player_count:
	print('Enter name for Player %d.' % current_player)
	current_player_name = raw_input('>')
	player_names.append(current_player_name)
	current_player += 1
'''

get_player_names_from_txt(player_names_source_txt)

# insert blank line
print('\n')

# Randomize the list of players in the list
shuffle(player_names)

# count the number of players in the list
player_count = len(player_names)

# Go through every single name in the list of player names and assign a board and a great power
for i in range(len(player_names)):

	# count the number of great powers in the list
	count_GP = len(great_powers)
	
	if (num_assigned_players % 7) == 0:
		current_board += 1
		print(horizontal_rule)
		print('Board %d: ' % (current_board))
	else:
		print('Board %d: ' % (current_board))
	
	# Determine whether or not the great powers list needs to be repopulated
	if count_GP == 0 and len(player_names) - i > 6:
		# if the great powers list has been depleted, and there are more than 6 players left to be assigned a great power, the list is repopulated with the names of the
		# original 7 great powers so that the next 7 players may be assigned a great power.
		great_powers = ['Austria-Hungary', 'France', 'Germany', 'Great Britain', 'Italy', 'Russia', 'Turkey']
		
	elif count_GP == 0 and len(player_names) - i == 6:
		# print message explaining special rules for a six player board
		print('\nSpecial rules for a six player board: Italian units hold in position and defend themselves, but do not support each other.  Units belonging to any of the players can support them in their holding position.  If Italian units are forced to retreat, they are disbanded.\nBoard %d:' % (current_board))
		# repopulate the great powers list with all of the original great powers save for Italy
		great_powers = ['Austria-Hungary', 'France', 'Germany', 'Great Britain', 'Russia', 'Turkey']
				
	elif count_GP == 0 and len(player_names) - i == 5:
		# print message explaining special rules for a five player board
		print('\nSpecial rules for a five player board: Italian and German units hold in position and defend themselves, but do not support each other.  Units belonging to any of the players can support them in their holding position.  If Italian or German units are forced to retreat, they are disbanded.\nBoard %d:' % (current_board))
		# repopulate the great powers list with all of the original great powers save for Italy and Germany
		great_powers = ['Austria-Hungary', 'France', 'Great Britain', 'Russia', 'Turkey']
			
	elif count_GP == 0 and len(player_names) - i == 4:
		# print message explaining the special rules for a four player board
		print('\nSpecial rules for a four player board: One player plays as England, the other three play the following pairs:\nAustria-Hungary & France\nGermany & Turkey\nItaly & Russia\n\nBoard %d:' % (current_board))
		# repopulate the great powers list according to the four player rules
		great_powers = ['England', 'Austria-Hungary & France', 'Germany & Turkey', 'Italy & Russia']
				
	elif count_GP == 0 and len(player_names) - i == 3:
		# print message explaining the special rules for a three player board
		print('\nSpecial rules for a three player board: One player controls England, Germany, and Austria.  The second player controls Russia & Italy.  The third player controls France & Turkey.\nBoard %d:' % (current_board))
		# repopulate the great powers list according to the three player rules
		great_powers = ['England, Germany & Austria-Hungary', 'Russia & Italy', 'France & Turkey']
		
	elif count_GP == 0 and len(player_names) - i == 2:
		# print message explaining the special rules for a two player board
		print('\nSpecial rules for a two player board: This board will function as a World War I simulation.  One player controls England, France, & Russia.  The second player controls Austria-Hungary, Germany, & Turkey. The game begins in 1914.  Before the Fall 1914 adjustments, flip a coin.  Italy joins the winner of the toss in Spring 1915.  The first player to control 24 supply centers wins.  This is also an enjoyable way for two new players to learn the rules.\nBoard %d:' % (current_board))
		# repopulate the great powers list according to the two player rules
		great_powers = ['England, France & Russia', 'Austria-Hungary, Germany & Turkey']
				
	elif count_GP == 0 and len(player_names) - i == 1:
		#Throw an exception because we should not have a 1 player board.
		print('\nERROR: You should not be seeing this message.  Earlier logic should have eliminated the possibility of a one player board\n')

	# count the number of great powers in the list
	count_GP = len(great_powers)

	# generate a random number between 0 and the number of random powers remaining
	GP_randomizer = random.randint(0,(count_GP - 1))

	# print the player's name and their assigned great power
	print(player_names[i] + '\t' + great_powers[GP_randomizer])

	# remove great power from the list
	great_powers.pop(GP_randomizer)
	
	# number of assigned players + 1
	num_assigned_players += 1
	
	# Insert a blank line to separate board assignments
	print('\n')

print('Boards & Great Powers have been assigned for all players.\n')
raw_input('Press any key to exit...')
