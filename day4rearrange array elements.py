a=[3,1,-2,-5,2,-4]
p=0
n=1
b=[0]*len(a)
for i in range(0,len(a)):
    if (a[i]>0):
        b[p]=a[i]
        p+=2
    else:
        b[n]=a[i]
        n+=2
print(b)        
