#Prime number generator
#Emil Davis
#01/27/15
#Last revision date 01/17/16

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
		print (testNum)
	testNum = testNum+2
	if testNum%5==0:
		testNum=testNum+2
#Debug "pause line"
#	raw_input("Press any key to continue")
