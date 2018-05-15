import random
import logging
import sys 

def Main():
	print '***** Welcome to the DICE Game *****\n'
	print "Press y/n Start/Stop Rolling the Dice: "
	while(True):
		val = sys.stdin.read(1)
		if val == 'y' or val == 'Y':
			print "You Got: %d" % random.randint(1,6)
			print "Press y/n to start/stop Rolling the Dice Again:"
		elif val == 'n' or val == 'N':
			print 'Thank You\n'
			sys.stdout.flush()
			break
if __name__ == "__main__":
	Main()
