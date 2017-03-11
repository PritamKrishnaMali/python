
import os, sys

sys.path.append("/home/pritam/python_program/")
print sys.path

if(0):
	import phone

	phone.isdn()
	phone.pots()
	phone.g3()

if(0):
	import phone
	phone.isdn.isdn()
	phone.pots.pots()
	phone.g3.g3()

if(1):
	import phone

	from phone import isdn
	from phone import pots
	from phone import g3
	
	isdn.isdn()
	pots.pots()
	g3.g3()
