def printfn(a):
    print(a)

a = 0.314E+1
b = 10+12j
c = 123
d = "123"

class zoo():
    def __init__(self, name):
        self.name = name
    
class dog(zoo):
    def __init__(self, name):
        super().__init__(name)

if a == 0.314:
    printfn(a)

while c < 125:
    printfn(c)
    c += 1
