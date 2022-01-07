def CheckPNZ(iNo):
	if iNo == 0:
		print("Number is Zero")
	if iNo > 0:
		print("Number is positive")
	if iNo < 0:
		print("Number is negative")		

def main():
	iValue = int(input("Enter a number \n"))
	CheckPNZ(iValue)

if __name__ == "__main__":
	main()