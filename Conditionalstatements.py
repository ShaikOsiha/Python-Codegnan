#Checking number is zero
n=int(input())
if n==0:
    print('Number is zero')
print('Program done')
#Product selection
stock=int(input())
price=int(input())
required_stock=int(input())
amount=int(input())
total_amount=price*required_stock
if required_stock<stock and total_amount<=amount:
    print("remaining amount:",amount-total_amount)
else:
    print("Insufficent")

#checking number is even or odd
n=int(input())
if n%2==0:
    print('Number is even')
else:
    print('Number is odd')
#checking number is even or odd
num=int(input())
if n%2:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#checking number is positive or negative
n=int(input())
if n>=0:
    print("Number is positive")
else:
    print("Number is negative")
#checking number is greater
num1=int(input())
num2=int(input())
if num1>num2:
    print(f"{num1} is greater")
else:
    print(f"{num2} is greater")

    

