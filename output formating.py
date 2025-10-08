#Output Formating
#1)old style
#2)Modulo operator
#3)Dot format
#4)f format


#1)old_style output formating
#No type conversion
name="Osiha"
age=22
print("Name is",name,"and age is",age)#not specified space_in output because of Camma,we get space

#expression in print
name="Osiha"
age=22
print("Name is",name,"and age is",age+3)

#2)Modulo Operator Output Formating
#%d=Integers
#%f=Float
#%s=string
name="Osiha"
age=23
print("Name is %s and age is %d"%(name,age))

#after interchanging then we get out as error
#name="Osiha"
#age=23
#print("Name is %s and age is %d"%(age,name))

#3)Dot format
name="Osiha"
age=22
print("Name is {} and age is {}".format(name,age))
print("Name is {} and age is {}".format(age,name))
print("Name is {1} and age is {0}".format(name,age+5))

#4)f format
name="osiha"
age=22
percentage=98.3457
print(f"name  is {name} and age is {age} and i have {percentage}")
print(f"name is {name} and age is {age} and i have{percentage:.2f}")


#leading zeroes in output with length 5
num=1
print(f"{num:0{5}d}")#d means integers
#in output we get space
num=1
print(f"{num:{5}d}")#because of 5  before not specified so defalt space
#zero is added in starting
num=10

print(f"{num:0{5}d}")


