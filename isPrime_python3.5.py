#01/26/16
#This program is to ask the user to input a number and conforms that number with the user.
#Checks to see if that number meets some basic criteria:
#	Is it a whole number? If not notify user.
#	Is it a zero? Notify user zero is not prime.
#	Is it a one? Notify user one is prime.
#	Is it a two? Notify user two is prime.
#	Is it negative? If it is negative, ask the user if they were looking for if the absolute value is prime.
#
#
#
#
#Ask the user for a number and store in memory:
numInput = input("Enter the number to test if it is prime: ")

#Check if the entered data was an integer:
#if type(numInput) != "'int'":
#	print "That wasn't a number!"

#print type(numInput)

#while (type(numInput) != int):
#	print "Fuck Yeah"

#Confirm the number with the user:
confirmBit = 0
while(confirmBit == 0):
	print ("You entered:", numInput)
	confirmYN = input("Is that correct (y/n)?")
	if confirmYN == 'y':
		confirmBit = 1
	elif confirmBit == 0:
		print ("Program Exited")
		quit()

#convert string input from user to an int
numInput=int(numInput)

#Is it negative?
#if numInput < 0:
#	absValYN = raw_input("The number you entered was NEGATIVE, do you want to test the absolute value?")


#Simple conditional tests
if numInput == 0:
	print ("You entered a ZERO which is not a natural number and cannot be prime. Deviding by ZERO is UNDEFINED.")
	quit()
elif numInput == 1:
	print ("You entered a ONE, of course it's PRIME!")
	quit()
elif numInput == 2:
	print ("You entered a TWO, of course it's PRIME!")
	quit()
elif numInput == 3:
	print ("You entered a THREE, of course it's PRIME!")
	quit()
elif numInput == 5:
	print ("You entered a FIVE, of course it's PRIME!")
	quit()
elif numInput%5 == 0:
	print ("You entered a number divisable by 5, of course it's NOT PRIME!")
	quit()
elif numInput%2 == 0:
	print (numInput, " is devisable by TWO which makes it an EVEN NUMBER, of course it's NOT PRIME.")
	quit()

else:
	print ("Performing calculations")
	
#Perform calcuations
	#Take inputted number and divide it by 2. Since it's odd the result is a float. Convert to int. Check if value is divisable witout a remainder.
	#This works but is too slow for larger numbers
	testDevisor = numInput / 2
	testDevisor = int(float(testDevisor))
	#print "testDevisor = ", testDevisor
	while (testDevisor > 1):
#		print "testDevisor = ", testDevisor
		if testDevisor == 2:
			print (numInput, "is PRIME!")
			quit()
		if numInput%testDevisor == 0:
			print (numInput, "is NOT PRIME.")
			quit()
		testDevisor = testDevisor - 1

	#Ok so start with faster idea
#Debug message
print ("Exited - no error")
