#Enter a number zero or non zero
n=int(input())
if n==0:
    print("Number is zero")
else:
    print("Number is non zero")

#Check whether number is divisible by 5
n=int(input())
if n%5==0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

#Check whether number is divisible by 4 or 5
num=int(input())
if num%4==0 or num%5==0:
    print(f"{num} is divisible by 4 or 5")
else:
    print(f"{num} is not divisible by 4 or 5")
#Check whether number is factor of 6 or not
num=int(input())
if num%6==0:
    print(f"{num} is factor of 6")
else:
    print(f"{num} is not factor of 6")

#checking wheather the element is present in list or not
a=[1,2,3,4]
num=5
if num in a:
    print(f"{num} is present in list")
else:
    print(f"{num} is not present in list")

 
