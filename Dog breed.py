class Dog:
    species = "Dog"  
    def __init__(self, name, breed):
        self.name = name    
        self.breed = breed  
Tommy = Dog("Tommy", "Pug")
Rocky = Dog("Rocky", "Beagle")
print("Tommy is a {}".format(Tommy.species))
print("Rocky is a {}".format(Rocky.species))
print("{} belongs to the {} breed ".format(Tommy.name,Tommy.breed))
print("{} belongs to the {} breed ".format(Rocky.name,Rocky.breed))