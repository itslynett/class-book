# Define the base class Animal
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Define a subclass for Dog
class Dog(Animal):
    def move(self):
        print("The dog is running 🐕")

# Define a subclass for Fish
class Fish(Animal):
    def move(self):
        print("The fish is swimming 🐟")

# Define a subclass for Bird
class Bird(Animal):
    def move(self):
        print("The bird is flying 🐦")

# Define a subclass for Car (Vehicles)
class Car:
    def move(self):
        print("The car is driving 🚗")

# Define a subclass for Plane (Vehicles)
class Plane:
    def move(self):
        print("The plane is flying ✈️")

# Test the polymorphism with different move actions
def test_move_action(animal_or_vehicle):
    animal_or_vehicle.move()

# Create instances
dog = Dog()
fish = Fish()
bird = Bird()
car = Car()
plane = Plane()

# Test polymorphism
test_move_action(dog)
test_move_action(fish)
test_move_action(bird)
test_move_action(car)
test_move_action(plane)
