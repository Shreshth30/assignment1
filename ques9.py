r=int(input("enter radius of circle "))
class circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
c=circle(r)
print(c.area())            