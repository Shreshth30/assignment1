def line(str):
    number=dict()
    words=str.split()
    for i in words:
        if i in number:
            number[i]+=1
        else:
            number[i]=1
    return number
print( line('our business is our business non of your business') )               