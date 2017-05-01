from sys import argv
script, argv1, argv2 = argv

def myfunction(x,y,z):
	print "Use %s spoons of grinds for %s coffees." % (x,y)
	print "Pour %s cups of hot water." % z
	print "Enjoy!\n"

myfunction(3.5, 3, 3)

water = 2
myfunction(water * 1.2, water, water)

myfunction(argv1, argv2, argv2)

Q1 = raw_input("spoons of coffee? ")
Q2 = raw_input("water? ")
myfunction(Q1, Q2, Q2)

myfunction("many", "hella", "a few")

myfunction(int(3.6), int(4.2), int(4))

myfunction("about %d" % 2, 3, "enough")

people = raw_input("how many people? ")
myfunction(int(people)*1.5, people, int(people)*1.8)