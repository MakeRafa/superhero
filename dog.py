class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")


    def bark(self):
        print("Woof!")

my_dog = Dog("jon", "SuperDog")
# my_dog.breed = "SuperDog"
# print(my_dog)
# print(my_dog.name)
print(my_dog.breed)
my_dog.bark()