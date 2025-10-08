#add(),remove(),discard(),update()_#s1.remove(100) #It raises Key Error if ele not present
s1={1,2,3,5,65,45}
s1.add(100)
s1.add(1)
print(s1)
s1.remove(100)
print(s1)
s1.discard(100)#no error it will give ele not present means
s1.discard(2)
print(s1)
s1.update({1,2,3})
print(s1)
