number = input('Enter the number : ')
number =  float(number)
change = 0.000000001
guess=0.3*number
while ((abs(guess**3)-number)>change):
	fx = guess**3-number
	fxx = 3*(guess**2)
	guess = guess - (fx/fxx)
print guess
