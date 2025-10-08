#string accessing and slicing
s="codegnan"
print(s[0])
print(s[-2])
print(s[-1])
print(s[2:5])
print(s[4:])
print(s[:4])
print(s[2:6:1])
print(s[-4: :-1])
print(s[:-5:-1])
print(s[::-1])
print(s[::1])

#empty string representation
s1=""
s2=str()#string function
#type()-this function returns the data type
print(type(s1))
print(type(s2))

#string operatos
#concadenation by using '+' operator
s1="code"
s2="gnan"
print(s1+s2)
print(s1+""+s2)


#string repetation using'*' operator
s1="code"
print(s1*3)
print(s1*10)

#string repetation using'*' operator
s1="code "
print(s1*3)
print(s1*10)

#string reading from user
s=input()
print("user enter input:",s)
#string convertion
s="TechMitra"
lower_string=s.lower()
print("Lower case conversion:",lower_string)
print("Upper case conversion:",s.upper())
print("Title case conversion:",s.title())

#find
#index
#count
s="codegnan"
print=(s.find("o")
print=(s.index("g")
print=(s.count("a")      

#strip
#lstrip
#rstrip
s="     Codegnan    "
print(s.strip())
print(s.lstrip())
print(s.rstrip())






