class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"Some Sound")

    def action(self):
        print(f"{self.name} is doing something.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")
    def action(self):
        print(f"{self.name} is chasing a mouse.")

if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Garfield")
    dog.speak()  # Buddy says Woof!
    cat.speak()  # Whiskers says Meow!
    dog.action()
    cat.action()