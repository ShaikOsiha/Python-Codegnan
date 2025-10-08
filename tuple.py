#Read  tuple integer from user
t=tuple(map(int,input().split()))
print(t)

#Index based and Slicing
t=(1,2,3,[10,20,30],"Codegnan")
print(t[2],t[-2],t[-4])
print(t[-1:2:-1])
print(t[3:-4:-1])


#single element representation in tuple _int output
t=(28)
print(type(t))

#single element representation in tuple and tuple output
t=(28,)
print(type(t))

#single element representation in tuple _int  and tuple output
t=(28)
t2=(10,)
print(type(t),type(t2))


#Tuple 2 Operations
#Concadenation Operation
t1=(1,2,3)
t2=('A',"b")
t3=t1+t2
print(t3)


#repetition Operation
t1=([1,2,3])
t=t1*3
print(t)


#Tuple Methods
t=(1,2,3,[10,20,30],"Codegnan")
ind=t.index(3)
count=t.count(3)
print(ind,count)

#Built infunction
#len(0,min(),max(),sum()
t=(1,2,3,4,5)
print(len(t),min(t),max(t),sum(t))

#string to tuple conversion
s="Codegnan"
print(list(s))
print(tuple(s))

#Tuple to list Conversion
t=(1,2,3,4,5)
print(list(t))













