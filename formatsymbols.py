ThisOne = "% S"
print "d - %d is a decimal integer." % 15
print "s - %s can display previously defined terms." % ThisOne
print "o - %o is the octal integer that represents 18. Isn't that cool?" % 15
print "x - %x is what? 230 in heX code, which is a base 16 expression!" % 230

print "Hex codes are easy. For example, 230 % 16 =", 230 / 16, "...", 230 % 16, "."
print "The 14 'cycles' mean 0123456789abcdef x 14. It has completed the full 'd' row in the table."
print "The 14 full rows can be expressed as e0. If this is confusing, think of how 'normal' base-10 numbers work:"
print "    1. They use the numerals 0-9"
print "    2. When your value complete the first 'row' in the table, you add a digit using the second numeral (1) to indicate row change"
print "    3. This is follwed by the first numeral (0) to indicate no additional value -- '10'."
print "Going back to our original number, 230, we had a remainder of 6."
print "This means 6 'places' after e0, so e1, e2, e3, e4, e5, e6 - 'e6' is our final hexadecimal number that is equal to 230."
print "X - %X is the same as 'x' but UPPERCASE." % 230
NewOne = "3 / 5"
print "r - %r is what? It prints the 'raw data' of the variable." % NewOne
