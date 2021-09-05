class Calculator:
    num = 10

    def __init__(self, a, b):
        self.firstNo = a
        self.secondNo = b
        print(" __init__ Parent Constructor called!")

    def intro(self):
        print("Hi")
        return None

    def addition(self):
        print("Addition is: ")
        return self.firstNo + self.secondNo + self.num

obj = Calculator(11,22)
print(obj.addition())