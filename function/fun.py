def fn():
	print "outside"
	def fn():
		return 10
	print fn()
	return 1111

print fn()
