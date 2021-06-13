x = int(input("Enter a number:"))
primeFlag = True
for i in range(2,x-1):
    if (x%i) == 0:
        primeFlag = False

if primeFlag:
    print("The entered number is a Prime Number")
else:
    print("The entered number is not a Prime Number")
