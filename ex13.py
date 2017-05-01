from sys import argv

script, first, second, third = argv

print "The script is called (\'script\' variable is your script/filename):", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "remember raw_input()?",
answer = raw_input()
print "your answer was:", answer

otherway = raw_input(
	"how about that other way to use raw_input? ")
print otherway, """ huh? Well, you define a variable = raw_input(\"prompt \") first.
Then you print using that variable you made.
"""