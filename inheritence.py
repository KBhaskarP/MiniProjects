class ANIMAL:
    def __init__(self):
        self.eyes=2
        self.alive=True
        
    def move(self):
        print("It moves")
        
    def eat(self):
        print("It eats fruits/Grains")
        
    def breathe(self):
        print("Inhale and Exhale")
        
class Fish(ANIMAL): #This fish class is a child of Animal class
    def __init__(self):
        super().__init__()#using super() we are basically accessing the super class features
        
    def move(self):
        super().move()#here using super() we are essentially accessing the super class methods along with the child class methods
        print("in water")
        
class Dog(ANIMAL):
    def __init__(self):
        super().__init__()
    def move(self):
        super().move()
        print("on ground")
        

class Bird(ANIMAL):
    def __init__(self):
        super().__init__()
        
    def move(self):
        super().move()
        print("in sky")
        
class Snake(ANIMAL):
    def __init__(self):
        super().__init__()
    def move(self):
        super().move()
        print("it crawls")
        
    
    
hebi=Snake()
print(hebi.eyes)
print(hebi.alive)
print(hebi.move())