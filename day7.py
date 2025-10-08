#split(pat)
s="The Sky is Blue and Ocean is Blue"
print(s.split())
print(s.split('Blue'))
print(s.split('u'))
print(s.split('zx'))


#join
l=['The','Sky','is',' Blue',' and',' Ocean', 'is',' Blue']
print("@".join(l))
print(" ".join(l))

#char()
#ord()
print(ord("A"))
print(chr(65))

#string checking functions
print("Codegnan".islower())
print("codegnan".isupper())
print("CODEGNAN".isupper())
print("Codegnan".isalpha())
print("CodeGnan".isalnum())
print("786".isalnum())
print("Codegnan".istitle())
print("56".isdigit())

#Membership operator(in,not in)
print("Y" in "Codegnan")
print("y" not in "Codegnan")


#string comparision
s1="abcd"
s2="abcde"
print(s1==s2)
print(s1>s2)
print(s1<s2)


#identity operator
#string comparision
s1="abcd"
s2="abcd"
print(id(s1),id(s2))
print(s1==s2)
print(s1>s2)
print(s1 is s2)


#built in function
print(len("Codegnan"))
print(min("Codegnan"))
print(max("Codegnan"))

#replace()
s="Codegnan"
print(s.replace('n','z'))
























