# Grabs the sys module; argv is 'arguments variable' feature
from sys import argv

# script is always the 1st variable for argv. filename is
# the only variable you'll be filling in.
script, filename = argv

# open() function opens the file that was entered in command line
# after the "python blabla.py "
txt = open(filename)

# %r, so the filename will be wrapped in quotes
print "Here's your file %r" % filename
# The . CALLS the read() FUNCTION on txt. read() displays
# the contents of the file.
print txt.read()
# Closing the file is important, so this was added in drill.
# However, python does not restrict you from opening a file
# more than once. (closing the file is like "File->Save...")
txt.close()

# Pretty straightforward
print "Type the filename again:"
# file_again variable is whatever the user enters after "> "
file_again = raw_input("> ")

# txt_again is equal to opening the user-entered filename
txt_again = open(file_again)

# Again, the read function is called on the file opened via
# txt_again.
print txt_again.read()
# Again, closing the open() during drill.
txt_again.close()