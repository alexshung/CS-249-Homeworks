import math
def infoCalculator(inputArr):
	total = 0.0
	for val in  inputArr:
		total += val
	retInfo = 0.0
	for val in inputArr:
		retInfo -= val*1.0 / total * math.log(val/total,2)
	return retInfo

inputArr =  list()
enteredNum =  "something"
while enteredNum != "done":
	enteredNum =  input("Enter a number \n")
	if enteredNum != "done":
		inputArr.append(float(enteredNum))
print(infoCalculator(inputArr))