#ifelif  check number is positive even/odd and negative even/odd
n=int(input())
if n%2==0 and n>0:
    print(f'{n} is positive even')
elif n%2==0 and n<0:
    print(f'{n} is negative even')
elif n%2!=0 and n>0:
    print(f'{n} is positive odd')
else:
    print(f'{n} is negative odd')


#nested if
n=int(input())
if n>=0:
    if n%2==0:
        print(f'{n} is positive even')
    else:
        print(f'{n} is positive odd')
else:
    if n%2:
        print(f'{n} is negative odd')
    else:
        print(f'{n} is negative even')

#ifelif  check three numbers which is greater
n1=int(input())
n2=int(input())
n3=int(input())
if n1>n2 and n1>n3:
    print('n1 is greater')
elif n2>n1 and n2>n3:
    print('n2 is greater')
else:
    print('n3 is greater')
#nested if
n1,n2,n3=map(int,input().split())
if n1>n2:
    if n1>n3:
        print(f'{n1} n1 is greater')
    else:
        print(f'{n3} n3 is greater')
else:
    if n2>n3:
        print(f'{n2} n2 is greater')
    else:
        print(f'{n3}  n3 is greater')

