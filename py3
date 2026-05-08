# Write a program that takes a string, string should be of even length. Divide the string into two
equals parts, check the number of vowels in both the parts of the string. If both parts of string have 
same number of vowels then return true otherwise return false.

# Testcase1	:  rebels
# Output     	:  true

def check(l):
    if len(l)%2!=0:
        return False
    else:
        m=len(l)//2
        p1=l[:m]
        p2=l[m:]
        n="aeiouAEIOU"
        c1=0
        c2=0
        for n in p1:
            c1+=1
        for n in p2:
            c2+=1
    return c1==c2   
    
l=input("enter string:")
print(check(l))


# Write a program that takes array of numbers as input, among the numbers in array,
check how many numbers starts with the same digit and ends with the same digits. 
Print the count of such kind of numbers in the given array.

# Testcase1	:  [ 34, 88, 423, 121, 2382, 10]
# Output     	:  3

def check(l):
    count=0
    for i in range(len(l)):
        s=str(l[i])
        if s[0]==s[-1]:
            count+=1
    return count
l=list(map(int,input("enter list:").split())) 
print(check(l))

# Write a program that takes array of numbers as input, among the numbers in array,
print the numbers which forms a prime number by adding one to it. 
Print such numbers in the given array separated b spaces.

# Testcase1	:  [ 7, 4, 7, 23, 10 ]
# Output     	:  4 10

def check(i):
    if i<2:
        return False
    for j in range(2,i):
        if i%j==0:
            return False
    return True        
    
l=list(map(int,input("enter number:").split()))
for i in range(len(l)):
    if check(l[i]+1):
        print(l[i])


#Write a program that takes a number as input, print the sum of duplicate numbers in the given number.
Testcase1	:  7473183
Output     	:  10

def check(n):
  f={}
  for i in str(n):
    if i in f:
        f[i]+=1
    else:
        f[i]=1
          
  total=0
  for j in f:
    if f[j]>1:
        total+=int(j)
  return total        
        
n=input("enter: ")
print(check(n))

Write a program that takes array of numbers as input and a number as second input.
Check the position of the factorial of the second input number in the given array.
Print the position of it. If the factorial of given second input number is not presented in the array
then print factorial of  the number is not presented.

Testcase1	:  [ 61, 4, 6, 7, 120 , 10 ]
Input :  5
Output     	: 4

def fact(n):
    m=1
    for i in range(1,n+1):
        m=m*i
    return m   
l=list(map(int,input("enter list: ").split()))
n=int(input("enter number: "))
f=fact(n)
if f in l:
    print(l.index(f))
else:
    print("not in list")


# Write a program that takes array of numbers are input, print the second duplicate number and it’s occurrence.

# Testcase1	:  [ 64, 1, 2, 7, 79, 7, 7, 1, 22]
# Output     	:  Second duplicate number is 7 and it is occurred 3 times
# Explanation	: In the given array [ 64, 1, 2, 7, 79, 7, 7, 1, 22], the second duplicate number is 7 and it is occurred for 3 times.


def check(n):
    f={}
    for i in n:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    d=[]
    for j in f:
        if f[j]>1:
            d.append(j)
    if len(d)>=2:
        second=d[1]
        print("second duplicate number is ",second,f[second])
    else:
        print("no second duplicate")
        
l=list(map(int,input("enter number: ").split()))
print(check(l))
