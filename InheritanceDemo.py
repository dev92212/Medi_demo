from ClassDemo import Calculator

class Child(Calculator):
    num2 = 20

    def __init__(self, aa, bb):
        print("I am a child class constructor")
        self.firstNo = aa
        self.secondNo = bb
        Calculator.__init__(self, self.firstNo, self.secondNo)

    def child_method(self):
        return self.addition() + self.num2

childobj = Child(11,22)
print(childobj.child_method())