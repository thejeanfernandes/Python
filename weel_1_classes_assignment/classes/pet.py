class Pet():
    """A simple class for representin a pet"""

    def __init__(self, name, age):
        """Initialize name and age variable/attributes"""
        self.name = name 
        self.age = age

    def clean(self):
        """Represent the act of cleaning the pet"""
        print(self.name + " is clean!")