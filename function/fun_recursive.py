fact = 1
def factorial(i):
	global fact 
	if (i == 1):
		return 1
	else:
		fact *= i
		factorial(i-1)

factorial(5)

