#SATURDAY TEST 1 (11/10/2025)

n1=int(input('Enter n1:'))
n2=int(input('Enter n2:'))
n3=int(input('Enter n3:'))
if( n1**2 + n2**2==n3**2) or (n1**2+n3**2==n2**2) or (n2**2+n3**2==n1**2):
    print("true")
else:
    print("false")


#equilateral,isocles,scalene triangle

n1=int(input('Enter n1:'))
n2=int(input('Enter n2:'))
n3=int(input('Enter n3:'))
if n1==n2==n3:
    print(f'{n1},{n2},{n3} sides are Equilateral')
elif n1!=n2!=n3!=n1:
    print(f'{n1},{n2},{n3} sides are Scalene')
else:
    print(f'{n1},{n2},{n3}sides are Isoscales')






#print total characters and digits in given string
s=' Code gnan @123'
char_count=0
digit_count=0
for i in range(len(s)):
    if s[i].isalpha():
        char_count +=1
    elif s[i].isdigit():
        digit_count +=1
print(char_count,digit_count)
    



#print only positive numbers

lst=[3,-1,5,0,-2]
res=[]
for i in range(len(lst)):
    if lst[i]>=0:
        res.append(lst[i])
print(res)   



