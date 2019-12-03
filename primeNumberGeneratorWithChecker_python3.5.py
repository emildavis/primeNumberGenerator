#Prime number generator
#Emil Davis
#01/27/15
#Last revision date 01/17/16
#updated revision 09/14/16 to update to Python 3.5 and an attempt to combine generator and checker
#will need to revisit using functions where I can just pass values

print ("1")
print ("2")
print ("3")
print ("5")
print ("7")

#divisorNum=3
testNum=11
while(True):
	divisorNum=3
#	testNum=11
	while(divisorNum<testNum/3):
		if testNum%divisorNum==0:
			break
		else:
			divisorNum=divisorNum+1
#			print testNum
#			break
	if testNum%divisorNum!=0:
		print ("Testing " + str(testNum))
		numInput = testNum
#	testNum = testNum+2
#	if testNum%5==0:
#		testNum=testNum+2
#Debug "pause line"
#	raw_input("Press any key to continue")
#ok, time to add the verify isPrime program

	if numInput%2 == 0:
		print (numInput, " is divisable by TWO which makes it an EVEN NUMBER, of course it's NOT PRIME.")
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
# print "testDevisor = ", testDevisor
			if testDevisor == 2:
				print (numInput, "is PRIME!")
			if numInput%testDevisor == 0:
				print (numInput, "is NOT PRIME.")
				quit()
			testDevisor = testDevisor - 1
	testNum = testNum+2
	if testNum%5==0:
 		testNum=testNum+2

