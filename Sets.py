#setexamples
s={1,2,34,20.5,"Codegnan",(1,2,3),1,2}
print(s)
#Empty set representation
s1={}
s2=set()#<class set>
print(type(s1),type(s2))
#read set of integers from user
s=set(map(int,input().split()))
print(s)
#in sets addition,repetition operations not possible
#set operations name
s1={1,2,"Hi","HELLO"}
s2={"Python",'java'}
print("Union:",s1.union())
print("Intersection:",s1.intersection(s2))
print("Difference:",s1.difference(s2))
print("Symmetric Difference:",s1.symmetric_difference(s2))
print("Subset:",s1.issubset(s2))
print("superset:",s1.issuperset(s2))
print("Disjoint set:",s1.isdisjoint(s2))

#set operators
s1={1,2,"Hi","HELLO"}
s2={"Python",'java'}
print("Union:",s1|s2)
print("Intersection:",s1&s2)
print("Difference:",s1-s2)
print("Symmetric Difference:",s1^s2)


