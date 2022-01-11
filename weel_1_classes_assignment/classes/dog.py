from classes.pet import Pet

class Dog(Pet):
    """A simple class for representation a dog"""
    
    def __init__(self, name, age, breed):
        """Initialize name and age variables/attribues for the dog"""
        super().__init__(name, age)
        self.breed = breed


    def placeDoginCarrier(self):
        """This represents the dog in a car carrier"""
        print(self.name + " is at the car carrer!")

    def taketoVet(self):
        """Represents the act of takin the dog to the vet"""
        self.placeDoginCarrier()
        self.visitVet

    def visitVet(self):
        """Contain all the tasks needed to take the dog to the vet"""
        print(self.name + " is on their way to the vet!")