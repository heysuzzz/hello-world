from sys import argv

print "Playing with sys module - argv."

#These arguments have to be entered in command line when running the script
_, first, second, third, fourth = argv

print "Welcome to", first, "School of", second, "and", third,"."

name = raw_input("Please enter your name: ")
number = raw_input("Please enter a number: ")
pet = raw_input("Please enter an animal name (singular): ")

print "Mr. or Ms. %s, your dormitory will be on the third floor - room %r." % (name, number)
print "Your %s will already be there." % pet
print "Have a %s semester!" % fourth