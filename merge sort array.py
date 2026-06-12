num1=[1,2,3,0,0,0]
num2=[3,4,5]
m=3
n=3
i=0
j=0
rev=[]
while (i<m and j<n):
    if num1[i]<num2[j]:
        rev.append(num1[i])
        i+=1
    else:
        rev.append(num2[j])
        j+=1
while i<m:
    rev.append(num1[i])
    i+=1
while j<n:
    rev.append(num2[j])
    j+=1
for k in range(m+n):
    num1[k]=rev[k]
print(num1)    
    
