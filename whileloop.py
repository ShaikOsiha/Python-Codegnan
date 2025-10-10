#print 1-n numbers using while loop
n=5
i=1
while i<n:
    print(i)
    i +=1
else:
    print("Program Done")


#2
n=5
i=1
while i<n:
    print(i,end="")
    i +=1
else:
    print("Program Done")
#3
n=5
i=1
while i<=n:
    print(i,end="    ")
    i +=1
else:
    print("Program Done")


#remove 2 from list
lst=[1,2,2,3,2,1]
ele=2
n=len(lst)
i=0
while i<n:
    if lst[i]==ele:
        lst.pop(i)
        n -=1

    else:
        i +=1
print(lst)



#Reverse of a number
n=456
res=0
while n>0:
    rem=n%10
    n=n//10
    res=res*10+rem
print(res)



#Total digits (length) of  number
n=1532#int(input())
count=0
while 0<n:
    rem=n%10
    count +=1
    n//=10
print(count)

#Amstrong number
n=153
length=0
temp1=temp2=n
while 0<temp1:
    rem=temp1%10
    length +=1
    temp1 //=10
res=0
while 0<temp2:
    rem=temp2%10
    res=res+rem**length
    temp2 //=10

if res==n:
    print(f'{n} is a armstrong number')
else:
    print(f'{n} is not a armstrong number')


#armstrong number 1 to 1000
armstrong_list=[]
for n in range(1,1001):
    length=len(str(n))
    temp2=n
    res=0
    while 0<temp2:
        rem=temp2%10
        res=res+rem**length
        temp2 //=10
    if res==n:
       armstrong_list.append(n)
print(armstrong_list)
