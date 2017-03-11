

import cal_menu
import sys
def simple():

	while (1):
		opt = cal_menu.sim_calc()
		
		if(opt >= 6):
			break

		if opt != 5:	
			num1 = input("Enter First The Number")
			num2= input("Enter Second The Number")	

		if(opt == 1):
			print num1 + num2
		elif(opt == 2):
			print num1 - num2
		elif(opt == 3):
			print num1 * num2
		elif(opt == 4):
			if(num2 == 0):
				num2 = input("Enter the Positive Number")
			print num1/num2	
		elif(opt == 5):
			return opt
		sys.stdin.read(1)
	return 5


while (1):
	opt = cal_menu.main_menu()
	if(opt >= 3):
		break
	if(opt == 1):
		simple()


		 
			
