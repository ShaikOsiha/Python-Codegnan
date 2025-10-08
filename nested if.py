#if elif
x=6
if x >= 10:
    print("High")
elif x >= 5:
    print("Medium")
else:
    print("Low")


#nested if
x=6
if x>=10:
    if x>=5:
        print('High')
    else:
        print('Medium')
else:
    print('Low')


#if elif
#Takes an integer n. Categorizes the number as: "small" if n is less than 10 and odd, "big" if n is 10 or more and even, "other" otherwise. 
n=28
if n<10 and n%2!=0:
    print('small')
elif n%2==0:
    print('big')
else:
    print('other')
    


#nested if
#Takes an integer n. Categorizes the number as: "small" if n is less than 10 and odd, "big" if n is 10 or more and even, "other" otherwise. Use nested if statements to implement the logic.
n=28
if n<10:
  if n%2!=0:
    print('small')
  else:
     print('other')
else:
  if n%2==0:
    print('big')
  else:
    print('other')


#if elif
#Takes an integer n. Returns "yes" if the number is divisible by 3 and greater than 5. Returns "no" otherwise. Use nested if statements.
num=10
if num%3==0 and num>5:
    print('yes')
elif num%3!=0:
    print('no')
else:
    print('Nothing')

#nested if
#Takes an integer n. Returns "yes" if the number is divisible by 3 and greater than 5. Returns "no" otherwise. Use nested if statements.
num=int(input())
if num%3==0:
  if num>5:
    print('yes')
  else:
    print('no')
else:
   if num%3!=0:
     print('no')
   else:
        print('Nothing')
















    
