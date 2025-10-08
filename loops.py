#print list in simple
nums=[1,2,3,4,5]
for val in nums:
    print(val)

#print list using for loop
lst=[2,5,6,7,8,9]
result=[]
for i in range(len(lst)):
    if lst[i]%2==0:
        result.append(lst[i])
print(result)        


#print list using for loop
lst=[2,5,6,7,8,9]
result=[]
for i in range(len(lst)):
    if lst[i]%2==0:
        result.append(lst[i])
    print(result)

#string for loop
veggies=['potato','brinjal','ladyfinger','cucumber']
for  veg in veggies:
    print(veg)

#Print each (individual char)char string print by for loop
str="bangalore"
for char in str:
    print(char)

#Print each (individual char)char string print by for loop
str="bangalore"
for char in str:
    print(char)
print('End')

#Print each (individual char)char string print by for loop ----search one letter
str="bangalore"
for char in str:
    if(char=="o"):
        print("o found")
        break
    print(char)
else:
    prinr("END")


#Print each (individual char)char string print by for loop ----search one letter
str="bangalore"
for char in str:
    if(char=="o"):
        print("o found")
        break
    print(char)
print("END")



#tuple for loop
tup=(1,2,3,4,2,8,9)
for num in tup:
    print(num)



#print the numbers using list for loop
num=[1,4,9,16,25,36,49,64,81,100]
for el in num:
    print(el)

#search for a number x in this  tuple ---for loop
num=(1,4,9,16,25,36,49,64,81,100,49)
x=49
inx=0
for el in num:
    if(el==x):
        print("Number found at inx",inx)
    inx +=1


#range in for loop
#1
for i in range(5):
    print(i)
#2
seq=range(5)
for i in seq:
    print(i)

#3

for i in range(10): #stop
    print(i)

#4
for i in range(0,10): #range(start,stop)
    print(i)
#5
for i in range(2,10):
    print(i)

#6
for i in range(0,10,2): #range(start,stop,end)
    print(i)

#print even numbers
for i in range(2,100,2):
    print(i)
#printod d numbers
for i in range(1,100,2): #see range 
    print(i)

#print numbers 1 to 100
for i in range(1,101):
    print(i)
#print numbers 100 to 1
for i in range(100,0,-1):
    print(i)
#print multiplication table of n

#1
n=int(input("enter number:"))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')

#2
n=int(input("enter number:"))
for i in range(1,11):
    print(n*i)

    






    


