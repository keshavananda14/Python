import logging
import sys
import random

def check(number, randnumber):
	if randnumber == number:
		print "Your Guess is Right"
		return 1
	elif number < randnumber and number >= (randnumber - 10):
		print "Your Guess is very little small"
	elif number < (randnumber - 11) and number >= (randnumber - 100):
		print "Your Guess is little small"
	elif number < (randnumber - 101):
		print "Your Guess is too small"
	elif number > randnumber and number <= (randnumber + 10) :
		print "Your Guess is very little large"
	elif number > (randnumber + 11) and number <= (randnumber + 100):
		print "Your Guess is little large"
	elif number > (randnumber + 101):
		print "Your Guess is too large"
	return 0
def Main():
	print "Note:\nvery little --> +/- 10\nlittle --> +/- 100\ntoo --> +/- More than 100\n"
	status = 0
	randNum = random.randint(1,1000)
	#print "randNum: %d " %(randNum)
	while(True):
		if status == 0:
			print "Please Input your Guess bewtween 1 to 1000"	
			num = input()
			status = check(num,randNum)
		elif status == 1:
			print "Thank you"
			break

if __name__ == "__main__":
	Main()
