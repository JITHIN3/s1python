
def hcf(a, b):
	if(b == 0):
		return a
	else:
		return hcf(b, a % b)

a = input("Enter First Number : \n")
b = input("Enter Second Number : \n")


print("The gcd of " +str(a) +" and " +str(b)+ " is : ", end="")
print(hcf(int(a),int(b)))
