import os
import Parse
import time


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
	desc = __import__(currentroom).Description
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
			if action == "clearscreen":
				os.system('cls' if os.name == 'nt' else 'clear')
				return currentroom
			elif action == "look":
				print desc
				return currentroom
			else:
				# Move or dont or do something
				try:
					func = getattr(__import__(currentroom), action)
		                except AttributeError:
					continue	
				else:
					changeroom, nextroom = func(command)
					if changeroom == 1:
						continuetoroom = 1
						return nextroom
					else:
						print "You cant go this way!"
						return currentroom


	
while 1 == 1 :
	result = room(currentroom)
#sets currentroom to the new room
	currentroom = result	


