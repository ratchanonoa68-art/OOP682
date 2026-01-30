class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"{self.name} is {self.age} years old. ")
        
def main():
    my_dog = Dog("buffy",3)
    my_dog.info()
    your_dog = Dog("joo",5)
    your_dog.info()