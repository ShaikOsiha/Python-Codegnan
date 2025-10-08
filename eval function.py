#Eval function
res=eval('5+2')
print(res)
print('5+2')#output 5+2
print(eval('5+2'))

#Integer
num=eval(input())
print(type(num),num)
#Float
num=eval(input())
print(type(num),num)
#string
num=eval(input())
print(type(num),num)
#list
num=eval(input())
print(type(num),num)
#dictionary
num=eval(input())
print(type(num),num)


#Reading 1 line input
s=input().strip().split()
print(s)
l=list(map(int,s))
print(l)
