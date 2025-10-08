#Type Conversion

#integer to float,bool,string conversion

num=int(input())
print(num)
#print(float(num))
val=float(num)
print(val)
print(bool(num))
print(str(num))



#float to integer,str,bool conversion
val=float(input())
print("Integer conv:",int(val))
print("String conv:",float(val))
print("Boolean conv:",bool(val))

#string to integer,float,boolean,list,tuple and set conversion
string=input()
print("Integer conv:",int(string))
print("Float conv:",float(string))
print("Boolean conv:",bool(string))
print("List conv:",list(string))
print("Tuple conv:",tuple(string))
print("Set conv:",set(string))


#list to string,tuple,set conversion
l=list(map(int,input().split()))
print(l)
print("String conv:",str(l))
print("Tuple conv:",tuple(l))
print("Set conv:",set(l))

#list to dictionary conversion
lst=[['a',1],['b',2],['c',3]]
print(dict(lst))

#tuple to list,string,set conversion
t=tuple(map(int,input().split()))
print("String conv:",str(t))
print("String conv:",str(t)[:5])
print("List conv:",list(t))
print("Set conv:",set(t))


#set to list,string,tuple onversion
s=set(map(int,input().split()))
print(s)
print("String conv:",str(s))
print("String conv:",str(s)[:5])
print("List conv:",list(s))
print("tuple conv:",tuple(s))




      







