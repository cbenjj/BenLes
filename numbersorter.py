import sys

def main(argv):
	if (len(sys.argv) != 2):
		sys.exit("enter one and only one number, you idiot!")
	if ((sys.argv[1]).isdigit() == False):
		sys.exit("learn what an integer is, then come back and enter one.") 
	if (int(sys.argv[1]) % 2 == 0):
		sys.exit("the number you entered is even.")
	if (int(sys.argv[1]) % 2 == 1):
		sys.exit("the number you entered is odd.")

if __name__ == "__main__":
	main(sys.argv[0:])
