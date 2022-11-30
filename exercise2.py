# num1=input("enter first number :")
# num2=input("enter second number :")
# num3=input("enter third number :")
# z=((num1)+(num2)+(num3))/3
# print(int(z))  # we can use string in place of int so output we get---->>4.0

# another method
num1,num2,num3 = input("enter three number comma seperated").split(",")
#(int(num1)+(num2)+(num3))/3----- average of three number

print(f"average of three number : {(int(num1) + int(num2) + int(num3)) / 3}")