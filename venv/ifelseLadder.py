mathsMark = int(input("Enter the mark scored in Maths:"))
physicsMark = int(input("Enter the mark scored in Physics:"))
chemistryMark = int(input("Enter the mark scored in Chemistry:"))

if (mathsMark >= 35 and physicsMark >= 35 and chemistryMark >= 35):
    averageMark = (mathsMark + physicsMark + chemistryMark)/3
    if averageMark  <= 59:
        print("The Grade is C and your average is ",averageMark)
    elif averageMark <= 69:
        print("The Grade is B and your average is ",averageMark)
    else:
        print("The Grade is A and your average is ",averageMark)
else:
    print("You have failed")





