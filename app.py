import time
class HelloWorld:
    def __init__(self, name: str="dear")->None:
        self.name=name
    
    def greating(self):
        return f"Hello my friend {self.name}"


name=input("Please Enter your name: ")

c=HelloWorld(name)
print(c.greating())
time.sleep(5)
