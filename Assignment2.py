def CheckEven(iNo):
	if iNo % 2 == 0:
		print(iNo,"Number is Even")
	else:
		print(iNo,"Number is odd")	

def main():
	print("Enter Number")
	iValue = int(input())
	CheckEven(iValue)


if __name__ == "__main__":
	main()