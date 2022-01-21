def getSum(n):

	sumOdd = 0
	sumEven = 0
	num = str(n)
	
	for i in range(len(num)):
		if(i%2 == 0):
			sumOdd = sumOdd+int(num[i])
		else:
			sumEven = sumEven+int(num[i])

	print("Sum Odd = ", sumOdd)
	print("Sum Even = ", sumEven)

if __name__ == "__main__":
	n = 54321
	getSum(n)

