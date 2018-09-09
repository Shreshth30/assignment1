line=[]
print("enter sequence of lines ")
while True:
    l=input()
    if l:
        line.append(l.upper())
    else:
        break
for l in line:
    print(l)            

