#When multiple conditions then if-elif-else
#checking three numbers which number is greater
num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print(f"{num1} is greater")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")
#When num1,num2 values are same then  condiition num1>=num2 with and between
num1=20
num2=20
num3=10
if num1>=num2 and num1>=num3:
    print(f"{num1} is greater")
elif num2>=num1 and num2>=num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

#Checking number  is (+even or -even) (+odd or -odd)
num=int(input())
if num%2==0 and num>0:
    print(f"{num} is +ve even")
elif num%2==1 and num>0:
    print(f"{num} is +ve odd")
elif num%2==0 and num<0:
    print(f"{num} is -ve even")
elif num%2==1 and num<o:
    print(f"{num} is -ve odd")
else:
    zero
