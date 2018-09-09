a=[5,7,9,3,2,1,4,2,6,3,0,9,8]
b=[]
for i in range(1,13):
    if(a[i]<5):
        print(a[i])
        b.append(a[i])
print(b)
n=int(input("enter a number "))
f=0
for j in b:
    if(b[j]==n):
        print("yes number is present ")
    else:
        f=1
if f==1:
    print("number is not present")              
                 