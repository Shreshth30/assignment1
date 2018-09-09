n=int(input("enter a number "))
def dtob(n):
    if n>1:
        dtob(n//2)
    print(n%2)
if __name__ == '__main__' :
    dtob(n)
    print        