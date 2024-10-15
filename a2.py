num1 = int(input("Enter your first value : "))
num2 = int(input("Enter your second value : "))
while(num2!=0):
    temp=num2
    num2=num1%num2
    num1=temp
hcf=num1
print("HCF of num1 and num2 is : " , hcf)