from classes.pet import Pet
from classes.dog import Dog
from classes.cat import Cat

my_dog = Dog("Scout", 3, "German Shepard")
print("My dogs name is: " + my_dog.name)
my_dog.clean()
print("My dogs breeed is: " + my_dog.breed)

my_cat = Cat("Fluffy", 3)
print("My cats name is: " + my_cat.name)


