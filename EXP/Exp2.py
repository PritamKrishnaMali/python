
import math
import os
import sys

opt = input("Enter The Option::")

if(opt == 1):
	number = input("Enter The Number::")
	
	print "Hexadecimal Number Of", number , "is", hex(number)
	print "Octal Number Of", number , "is", oct(number)
elif (opt == 2):
	print math.pi
	print math.sin(90)
elif(opt == 3):
	os.system("clear")
elif(opt == 4):
	print sys.version
	print sys.subversion	
elif(opt == 5):
	os.chdir("/home/pritam/Training")
	print os.getcwd()
elif(opt == 6):
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
	print int(sys.argv[1]) + int(sys.argv[2])
 
