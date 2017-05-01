player = raw_input("Enter your name, stranger: ")

age = int(raw_input("How many years have you spent on this earth? "))
if 14 <= age <= 99999:
	print """\n\tWelcome to the abandoned dungeon.
	Pray you tread lightly, lest you wake the dormant spirits
	that hunger for stray souls to feed upon.\n"""
	print "You push open the heavy doors and see a bloodstained table."
	print "On the table are a crowbar and a lamp. Which do you take?"
	print "1. Crowbar\n2. Lamp\n3. Both"
	
	item = raw_input("> ")
	if item == "1":
		print "You use the crowbar to pry open a large wooden crate."
		print "But it's too dark to see anything. What do you do?"
		print "1. Go back to the table to fetch the lamp.\n2. Reach in to feel for any items that may be inside."

		crate = raw_input("> ")
		if crate == "1":
			print "You go back for the lamp on the table, but notice that a bony arm now rests on the table."
			print "You barely have time to process the rotting face the arm is attached to before its jaws close upon your skull."
		elif crate == "2":
			print "You reach in as deep as you can, but find no bottom; you lose your balance and fall into the unseen abyss."
			print "The last thing you see before darkness consumes you is the crate closing itself above you."
		else:
			print "You decided to think outside the... crate. You may have avoided a certain death this day; goodbye, %s." % player

	elif item == "2":
		print "You take the lamp and walk down the narrow hallway."
		print "You find another heavy door at the end of the hallway, much like the one at the entrance -- except this one has a plaque."
		print "When the lamplight falls on the plaque, you jump back; it says \"%s\"." % player
		print "Before you can turn around and run, the door is yanked open and a pair of hands push you inside."
		print "The door closes just as quickly as it opened; your screams from inside your coffin does not echo out to the world of the living."

	elif item == "3":
		print "You use the crowbar to pry open a large wooden crate."
		print "The lamp illuminates the interior, and you realize that the crate was hiding a trapdoor to a small room under the floor."
		print "You try to decide whether or not you've satisfied your curiosity and that this is a good time to leave."
		
		time = int(raw_input("How many minutes do you consider your options for? "))
		if time <= 5:
			print "You make up your mind quickly and leave the dungeon. Goodbye, %s..." % player
		else:
			print "Intruders who linger must not have great attachment to the world of the living. You, %s, are now one of us, the living dead. Welcome to the eternity..." % player

	else:
		print "You decide that this little exploration may be more than what you bargained for, and leave the dungeon. Goodbye."

	
else:
	print "The abandoned dungeon is a spooky place not suitable for young minds like yours. Goodbye."