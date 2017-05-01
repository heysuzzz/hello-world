def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a + b

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b

def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b

def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b


print "Let's do some math with just functions!"

# When the function is assigned to the variable, the
# value of the function is assigned to the variable as well.
age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

# So, by calling the functions to assign values to variables,
# two things happen:
# 1) the function runs, which is why the CAPS text prints;
# 2) the resulting value is assigned to the variable,
# which is why it fills in the following string.
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "\n", add(30, 5) # This prints as expected.
print age    # Where is the CAPS text for this??
print "wtf? %d" % age    # Where is the CAPS text for this??

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes ", what, "Can you do it by hand?"