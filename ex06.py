# The variable x is defined. %d displays an integer number
x = "There are %d types of people." % 10
# The variable 'binary' is defined as the string "binary"
binary = "binary"
# The variable do_not is defined as the string "don't"
do_not = "don't"
# The variable y is defined as a string that contains 2 %s format characters. Each is defined as a previously defined variable.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#using %r instead of %s displays the same thing in quotes. "raw data"
print "I said: %r." % x
#here, %s is used, so it needs quotes typed in.
print "I also said: '%s'." % y

#apparently False with a capital F is not considered text
hilarious = False
# joke_evaluation is defined here; the format character %r can be "filled in" later when the variable joke_evalutaion is actually used.
joke_evaluation = "Isn't this joke so funny?! %r"

#here, the %r within joke_evaluation is "defined as" (or, told to display) the variable hilarious.
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# I guess you can also use plus instead of comma to concatenate stuff
print w + e