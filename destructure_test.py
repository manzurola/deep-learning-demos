class MyClass:
    myvar1 = None
    myvar2 = None

    def __init__(self):
        self.myvar1 = 5
        self.myvar2 = 10

c = MyClass()

myvar1, myvar2 = c

print(myvar1)
print(myvar2)
