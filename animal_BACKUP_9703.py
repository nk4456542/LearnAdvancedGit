import sys

<<<<<<< HEAD
def cat():
	print('meow')
=======
def dog():
	print('Woof')
>>>>>>> dog

def default():
	print('hello')


def main():
<<<<<<< HEAD
	if sys.argv[1]=='cat':
		cat()
	else:	
=======
	if sys.argv[1]=='dog':
		dog()
	else:
>>>>>>> dog
		default()

if __name__ == '__main__':
	main()

