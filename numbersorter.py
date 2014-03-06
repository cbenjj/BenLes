# just a testing program to check if a number is prime

import sys
import math

def isPrime(number):
	if number > 1:
		squareRootOfNumber = int(math.sqrt(number))
		for i in range(2, squareRootOfNumber):
			if number % i == 0:
				return False
		return True
	else:
		return False

def main(argv):
	if (len(sys.argv) != 2):
		sys.exit("enter one and only one number, you idiot!")
	try:
		inputNumber = int(sys.argv[1])
	except ValueError:
		sys.exit("learn what an integer is, then come back and enter one.")

	if (inputNumber % 2 == 0):
		print "the number you entered is even"
	else:
		print "the number you entered is odd"

	if (isPrime(inputNumber)):
		print "and it is prime!"
	else: 
		print "and it is not prime!"

if __name__ == "__main__":
	main(sys.argv[0:])
