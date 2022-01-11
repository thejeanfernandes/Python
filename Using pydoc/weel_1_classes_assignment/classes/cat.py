from classes.pet import Pet

class Cat(Pet):
    """A simple class for representation a dog"""
    
    def __init__(self, name, age):
        """Initialize name and age variables/attribues for the dog"""
        super().__init__(name, age)