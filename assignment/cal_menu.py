#Calculator Menu 
#Author::Pritam Krishna Mali
#Date:: 09/03/2017

import os

def main_menu():
	'''This is main menu of Calculator'''
	
	os.system("clear")
	print "\n\n"	
	print "CALCULATOR".center(30,'*')
	
	print "1.Simple Calculator"
	print "2.Scientific Calculator"
	print "3.Exit"
	
	opt = input("\nEnter The Option::")

	return opt

def sim_calc():
	'''This is menu of simple calculator'''
	
	os.system("clear")
	
	print "\n\n"
	print "Simple Calculator".center(30,'*')
	print "1.add"
	print "2.sub"
	print "3.mul"
	print "4.div"
	print "5.go back"

	opt = input("\nEnter The Option::")

	return opt

def sci_calc():
    '''This is menu of Scientific calculator'''

    os.system("clear")

    print "\n\n"
    print "Scientific Calculator".center(30,'*')
    print "1.sin"
    print "2.cos"
    print "3.sqrt"
    print "4.power of"
    print "5.go back"

    opt = input("\nEnter The Option::")

    return opt





