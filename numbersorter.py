import sys

def main(argv):
	if (len(sys.argv) != 2):
		sys.exit("enter one and only one number, you idiot!")
	try:
		inputNumber = int(sys.argv[1])
	except ValueError:
		sys.exit("learn what an integer is, then come back and enter one.")

	if (inputNumber % 2 == 0):
		sys.exit("the number you entered is even.")
	if (inputNumber % 2 == 1):
		sys.exit("the number you entered is odd.")

if __name__ == "__main__":
	main(sys.argv[0:])
