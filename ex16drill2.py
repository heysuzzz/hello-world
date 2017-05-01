from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# extra 'w' parameter is passed to open it in overwrite mode.
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# technically not necessary because 'w' (overwrite mode).
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# As I found out, write() only takes 1 argument.
# To reduce the redundancy below, I could instead write:
# alternative = (line1, "\n", line2, "\n", line3, "\n")
# target.write(alternative)
# Or I can make it even shorter, like this:
target.write("%s%s%s%s%s%s" %(line1, "\n", line2, "\n", line3, "\n"))

print "And finally, we close it."
target.close()