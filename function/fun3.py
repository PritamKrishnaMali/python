def test12(*pos, **kwd):
	print "Positional", pos
	print "Keyword", kwd

test12(10, 20, a=30, b=40)
test12(10, 20)
test12(a=30, b=40)
test12()
