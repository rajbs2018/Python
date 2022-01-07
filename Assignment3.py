def Add(iNo1 , iNo2):
	add = iNo1 + iNo2
	return add

def main():
	iValue1 = int(input("Enter First number"))
	iValue2 = int(input("Secound Number"))
	ret = Add(iValue1 ,iValue2)
	print("result is",ret)


if __name__ == "__main__":
	main()