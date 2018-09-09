class student():
    def __init__(self):
        self.str=""
    def getstring(self):
        self.str=input("enter your string ")
    def printstring(self):
        print(self.str.upper())
str=student()
str.getstring()
str.printstring()                