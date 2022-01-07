def Even(iNo):
	for i in range(0,iNo+1,2):
		print(i)

def main():
	iValue = int(input("Enter number \n"))
	Even(iValue)

if __name__ == "__main__":
	main()