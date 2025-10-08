#total seconds to hours,minutes,seconds
sec=10000
h=sec//3600
min_sec=sec-h*3600
min=min_sec//60
s=min_sec-min*60
print(h,min,s)

#time to seconds
h=int(input())
m=int(input())
s=h*60*60+m*60
print(s)
#hours
s=10000
m=int(input())
h=s//3600
m=m%60
print(h)

#minutes
m=int(input())
m=m%60
print(m)
