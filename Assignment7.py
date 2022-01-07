def Div(iNo):
	if iNo % 5 == 0:
		print("True")
	else:
		print("False") 


def main():
	iValue = int(input("Enter number \n"))
	Div(iValue)

if __name__ == "__main__":
	main()