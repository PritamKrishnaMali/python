
dct1 = {10:20, "Pritam":99}

print dct1

def dcttest(dct2):
	dct2[10] = 50
	dct2["Pritam"]+= 3
	print id(dct2)			#Reference is same
	print dct2

dcttest(dct1)
print id(dct1)
print dct1
