################################
###  			     ###
###   	   IBM_TEXT.PY       ###
###   			     ###
################################

import os
import Parse
import time
import sys


os.system('cls' if os.name == 'nt' else 'clear')
print " ______________  ___    _____  _   _ _____ ___________ _   _ "
print "|_   _| ___ \  \/  |   |_   _|| \ | |_   _|  ___| ___ \ \ | |"
print "  | | | |_/ / .  . |     | |  |  \| | | | | |__ | |_/ /  \| |"
print "  | | | ___ \ |\/| |     | |  | . \`| | | | |__ | |  /| . \ |"
print " _| |_| |_/ / |  | |    _| |_ | |\  | | | | |___| |\ \| |\  |"
print " \___/\____/\_|  |_/    \___/ \_| \_/ \_/ \____/\_| \_\_| \_/"
print "                                                "
print "                    _____       _____           "
print "                   / __  \     |  _  |          "
print "                   \`'/ /'     | |/' |          "
print "                     / /       |  /| |          "
print "                   ./ /___  _  \ |_/ /          "
print "                   \_____/ (_)  \___/           "
print "                                                "
time.sleep( 1 )
os.system('cls' if os.name == 'nt' else 'clear')


print ""
print ""
print ""
print ""
print ""
print ""
print "                  READY PLAYER ONE?"


time.sleep( 2 )
os.system('cls' if os.name == 'nt' else 'clear')




###########################
# START OF ACTUAL PROGRAM #
###########################

currentroom = "null"
currentroom = "room1"
inventory = {
	'gold' : 0,
	'popcorn' : 0,
	'backpack' : [],
	'trophys' : []
}

def room(currentroom):
	continuetoroom = 0
	name = __import__(currentroom).Name
	show_desc = __import__(currentroom).Visited
	desc = "Description"
	descfunc = getattr(__import__(currentroom), desc)
	desc = descfunc() 
	print name
	if show_desc == 0:
		print desc
		__import__(currentroom).Visited = 1
	while continuetoroom == 0:
		print ">",
		command = raw_input()
	
		action = Parse.action(command)
	
		item = Parse.item(command)
	

	
		if action == "Im sorry, I dont understand that.":
			print action
		else:
			# GAME WIDE COMMANDS

#####################  CLEAR  ########################
			if action == "clearscreen":
				os.system('cls' if os.name == 'nt' else 'clear')
				return currentroom
			
######################  LOOK  #########################
			elif action == "look":
				desc = descfunc()
				print desc
				return currentroom
			
####################  INVENTORY  #######################
			elif action == "inventory":
				print " INVENTORY "
				print "-----------"
				print "Gold:", inventory['gold']
				print "Backpack:", ', '.join(inventory['backpack'])
				print "Tropheys:", ', '.join(inventory['trophys'])
				print "Remaining Popcorn:", inventory['popcorn']
				print
				return currentroom


######################  GET  ###########################
			elif action == "get":
				if item == 0:
					print "What do you want to get?"
				elif item == "gold":
					try:
						if "gold" in __import__(currentroom).items:
							if __import__(currentroom).items['gold'] > 0:
								amount = __import__(currentroom).items['gold']
								inventory['gold'] = inventory['gold'] + amount
								__import__(currentroom).items['gold'] = 0
								print "Taken"
							else:
								print "There is no gold here."
					except AttributeError:
						print "There is no gold here."
				else:
					print "You cant get that."

#######################  MAKE  ###########################
			elif action == "make":
				if item == 0:
					print "What do you want to make?"
				elif item == "popcorn":
					counter = 11
        				print "popping..."
        				original = counter
       					while counter > 0:
                				length = original - counter
                				progressbar = ("=" * 4) * length

                				numofwhite = counter - 1
                				white_space = (" " * 4) * numofwhite

                				percent_done = (length / (original - 1)) * 100
                				percent_done = round(percent_done)

                				print progressbar, white_space, percent_done, "%              \r",
                				sys.stdout.flush()

                				time.sleep( .25 )
                				counter -= 1
        				else:
                				print
                				print "100 popcorn added to bin!"
                				inventory['popcorn'] = inventory['popcorn'] + 100
				else:
					print "You cant make that."

			elif action in __import__(currentroom).specials:
				print
				try:
					func = getattr(__import__(currentroom), __import__(currentroom).specials[action])
				except AttributeError:
					continue
				else:
					func()
					return currentroom


			else:
				# Move or dont or do something
				try:
					nextroom = __import__(currentroom).directions[action]
		                except KeyError:
					print "You cant go this way!"
					continue	
				else:
						continuetoroom = 1
						return nextroom
					


	
while 1 == 1 :
	result = room(currentroom)
#sets currentroom to the new room
	currentroom = result	


