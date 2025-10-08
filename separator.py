#Example1
a = input()
b = input()
separator = input()[0]

########### Write your code below ###############

# Print with space
print("a,b")

# Print without newline at the end
print(a,b,end="")

# Print with separator
print(f'{a}{separator}{b}')

# Print without space
print(f'{a}{b})
#Example2
#string repitition
a = input()
n = int(input())
#code here
print(a*n)

#Example3
a = input()
b = input()
c = input()
# Write your code below that prints a a times and b b times, seperated by c
print(f'{a*int(a)}{c}{b*int(b)}')

#Example4
      #User function Template for python3
s=input()
n=int(input())
f=float(input())
########### Write your code below ###############

# Take string input and print the string input
print(s)

# Take integer input and add 10 to the integer input and print
print(n+10)

# Take floating-point input and multiply the float input by 10 and print
print(f*10)




