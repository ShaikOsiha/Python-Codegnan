#Reading dictionary from user
n=int(input())
d={}
for i in range(0,n,1):
    key,value=map(int,input().split())
    d[key]=value
print(d)

#update in dictionary(adding)
n=int(input())
d=dict()
for i in range(n):
    key,value=map(int,input().split())
    d.update({key:value})
print(d)


#Total seconds to hours,minutes,seconds
sec=10000
h=sec//3600
min_sec=sec-h*3600
min=min_sec//60
s=min_sec-min*60
print(h,min,s)


