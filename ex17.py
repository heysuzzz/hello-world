from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# Nixed the standalone Open variable to shrink 2 lines to 1:
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

open(to_file, 'w').write(indata)

print "Alright, all done."

# I commented out the 2 close calls bc I edited ^ so that
# there's no variable that's purely an open object.
# out_file.close()
# indata.close()