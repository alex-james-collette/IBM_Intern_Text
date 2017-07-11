##################################
###                            ###
###           PARSE.PY         ###
###                            ###
##################################

def action(command):
# Default Variable Assignment
	action = "Im sorry, I dont understand that."
	item = ""

	command = command.lower()

# Direction commands
	if len(command) == 1 and command == 't' or command == "tests":
		print "debug!!"
		time.sleep( 2 )





	if len(command) == 1 and command == 'n' or command.find("north") != -1:
		if command.find("west") != -1:
			action = "northwest"
		elif command.find("east") != -1:
			action = "northeast"
		else:
			action = "north"
	
	if len(command) == 1 and command == 's' or command.find("south") != -1:
                if command.find("west") != -1:
                        action = "southwest"
		elif command.find("east") != -1:
			action = "southeast"
                else:
                        action = "south"


	if len(command) == 1 and command == "e" or command.find("east") != -1:
		if command.find("north") != 0 and command.find("south") != 0:
			 action = "east"		
	
	if len(command) == 1 and command == "w" or command.find("west") != -1:
		if command.find("north") != 0 and command.find("south") != 0:
			action = "west"	
	
	if len(command) == 2:
		if command == "nw":
			action == northwest
		if command == "sw":
			action == southwest
		if command == "ne":
			action == northeast
		if command == "se":
			action == southeast




# Action commands
	if command.find("look") != -1:
                action = "look"
	
	if command.find("get") != -1:
                action = "get"
	
	if command.find("attack") != -1:
                action = "attack"

# Special commands
	if command.find("clear") != -1:
		action = "clearscreen"


# Finish
	return action




##########################  ITEM  #########################



def item(command):

	command = command.lower()

# Sort Actions

	if command.find("north") != -1 or command.find("south") != -1 or command.find("east") != -1 or command.find("west") != -1:
		item = 0


#Add elif for each possible item.

	elif command.find("badge")!= -1:
		item = "badge"

# If no item
	
	else:
		item = 0

#Finish

	return item
	








