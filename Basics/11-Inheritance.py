class Animal:
    def __init__(self, habitat):
        self.habitat =  habitat
    
    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self):
        super().__init__("Kennel")

    def sound(self):
        print('Woof!Woof!')

x = Dog()
x.print_habitat()
x.sound()
y=Animal("Kennel in parent class")
y.print_habitat()
y.sound()
