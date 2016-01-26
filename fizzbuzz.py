from sys import argv


def fizzbuzz(userinput):
    for x in xrange(1, userinput + 1):
        if x % 2 == 0 and x % 3 == 0:
            print "fizzbuzz"
        elif x % 2 == 0:
            print "fizz"
        elif x % 3 == 0:
            print "buzz"
        else:
            print x

try:
    fizzbuzz(int(argv[1]))
except ValueError:
    print "That wasn't an integer!"