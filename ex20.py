from sys import argv

script, input_file = argv

# "read" reads everything in the input file to a certain
# size (bytes) unless no size is designated.
def print_all(f):
	print f.read()

# "seek" moves the reference point to the
# beginning of the file = 0. (1 = current position; 2 = end)
def rewind(f):
	f.seek(0)

# "readline" reads one entire line from the file;
# a trailing newline is kept at the end.
def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)