
int1 = 10
print int1

def inttest(int2):
	int2 = 20 
	print int2
	print id(int2)

inttest(int1)
print int1
print id(int1)

