
def test1():
	'''This Function is Test1 Function'''
	return "I am In Function test1"

def test2(a, b):
	'''This Function is Test2 Function'''
	print a, b

def test8(a, b=30):
	print a, b

x = 100
print x

def test10(): 
	'''This Is Normal Local Variable Explanation Example'''
	print x

x = 100 
print x

def test11():
	global x
	x = 200
	print x


test11()
print x
#test10() 
#print x

#test1()
#test2(10, 20)
#test8(a, b)


