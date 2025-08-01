class myclass:
    __privateVar = 27;
    def __privateMeth(self):
        print("I am in my class")
    def hello(self):
        print("Private variable value",myclass.__privateVar)
obj = myclass()
obj.hello()
obj.__privateMeth