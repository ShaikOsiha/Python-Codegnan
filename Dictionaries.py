#Dictionaries
d={1:"A","A":1,"Hi":"Hello",(1,2,3):(10,20,30),12.241:10.00}
print(d)

#duplicatee keys
d={1:"A","A":1,"Hi":"Hello",(1,2,3):(10,20,30),12.241:10.00,1:"z"}
print(d)


#list can't be used as a Key
#d={1:"A","A":1,"Hi":"Hello",[1,2,3]:(10,20,30),12.241:10.00,1:"z"}
#print(d)______error


#values access by passing keys
d={1:"A","A":1,"Hi":"Hello",(1,2,3):(10,20,30),12.241:10.00,1:"z"}
print(d[1])
print(d["A"])
#update values and items
d={1:"A","A":1,"Hi":"Hello",(1,2,3):(10,20,30),12.241:10.00,1:"z"}
d[1]="x"
print(d[1])
d['1']='x'
print(d['1'])
print(d)

#Empty dictionary  representation
d1={}
d2=dict()
print(type(d1),type(d2))

#Dictionary Methods
#get(key,default)
d={1:"A","A":1,"Hi":"Hello",(1,2,3):(10,20,30),12.241:10.00,1:"z"}
print(d.get(1))
print(d.get(10))
print(d.get(10,'Key is not present'))
print(d.get(10,0))

#update(new_dict)
d1={"batch":39,"Course":"PFS"}
d2={"Course":"JFS","lang":"java"}
d1.update(d2)
print(d1)

#popitem(),pop(key),clear()
d={"batch":39,"Course":"PFS","lang":'Python'}
print(d.popitem())
print(d.pop('Course'))
print(d)
d.clear()
print(d)
#key(),values(),items()
d={"batch":39,"Course":"PFS","lang":'Python'}
print(d.keys())
print(d.values())
print(d.items())

#Dictionary to list
d={"batch":39,"Course":"PFS","lang":'Python'}
print(list(d.keys())[0])







