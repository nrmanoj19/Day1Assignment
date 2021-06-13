x = int(input("Enter a number of your choice"))
i = 0
while(i<x):
    i+= 1

    if(i>=100):
        break

    if (i % 10) == 0:
        continue
    print(i)

