#Expriments

opt = input("Enter The Option:")

if opt >= 5 or opt == 0:
	print "Wrong Option"
if opt==1:
	no = input("Enter The Number")
	
	if no==100:
		print "Number Is Equal To 100"
	elif no > 100:
		print "Number Is greater than 100"
	else:
		print "Number is less than 100"
elif opt == 2:
	i = 1
	while i<=10:
		print i
		i +=1
elif opt == 3:
	i = 1
	while i<=10:
		print i
		i +=1
		if i == 6:
			break
elif opt == 4:
	i = 1
	while i<=10:
		if i == 5:
			i += 1
			continue
		print i
		i +=1
elif opt == 5:
	day = raw_input("Enter The Day:")

	if day == "sunday":
		print "Cloth Wash"
	elif day == "saturday":
		print "playing cricket"
	elif (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday"):
		print "Stupid fello go to office"
	else:
		print "wrong input"
	 
	


	



 
		
