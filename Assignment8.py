def Pattern(iNo):
	for i in range(iNo,end=" "):
		print("*\t")

def main():
	iValue = int(input("Enter a number to print a star \n"))
	Pattern(iValue)

if __name__ == "__main__":
	main()