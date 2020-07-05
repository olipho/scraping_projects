# HCF add prime factors to a list, not including repeats
# LCM include repeats

while 1:
	menu = "What would you like to do? \n 1. Find a highest common factor \n 2. Find a lowest common multiple \n 3. Find both HCF and LCM \n 9. Exit\n Enter an option."

	x = int(input(menu))

	factor_lista = []
	factor_listb = []
	multiple_lista = []
	multiple_listb = []	

######### Find the Highest Common Factor
	if x == 1: 
		y = int(input("Enter the first number ")) 
		z = int(input("Enter the second number "))
		if y <= 0 or z <= 0:
			print("Not a valid input. Please choose a positive integer.")
		else:
			for i in range(1, y+1):
				if y % i == 0:
					factor_lista.append(i)
			
			for j in range(1, z+1):
				if z % j == 0:
					factor_listb.append(j)	
		
			hcf = max(set(factor_lista).intersection(factor_listb))	

			print("The highest common factor is " + str(hcf))
			
########Find the lowest common multiple    
	elif x == 2: 
		a = int(input("Enter the first number  ")) 
		b = int(input("Enter the second number "))
		if a <= 0 or b <= 0:
			print("Not a valid input. Please choose a positive integer.")
		else:
		###c gives the number at which the list needs to stop ###
			c = a * b
			for j in range(1, c+1):
				multiple_lista.append(j * a)	
			for k in range(1, c+1):
				multiple_listb.append(k * b)		

			lcm = min(set(multiple_lista).intersection(multiple_listb))	

			print("The lowest common multiple is " + str(lcm)) 

#######FINDING BOTH####################
	elif x == 3:
		y = int(input("Enter the first number ")) 
		z = int(input("Enter the second number "))
		if y <= 0 or z <= 0:
			print("Not a valid input. Please choose a positive integer.")
		else:
			for i in range(1, y+1):
				if y % i == 0:
					factor_lista.append(i)
			
			for j in range(1, z+1):
				if z % j == 0:
					factor_listb.append(j)
		
			hcf = max(set(factor_lista).intersection(factor_listb))	
    
			#c gives the number at which the list needs to stop
			c = y * z
			for i in range(1, c+1):
				multiple_lista.append(i * y)	
			for j in range(1, c+1):
				multiple_listb.append(j * z)		

			lcm = min(set(multiple_lista).intersection(multiple_listb))	

			print("The highest common factor is " + str(hcf) + " and the lowest common multiple is " + str(lcm)) 
###########################

	elif x == 9:
		print("Good bye!")
		break

	else:
		print("Not a valid input. Try again.")