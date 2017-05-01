from sys import argv

script, filename = argv

target = open(filename, 'w')

target.write(raw_input("type something: "))
target.close()