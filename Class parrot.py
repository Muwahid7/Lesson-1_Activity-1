class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
Ruby = parrot("Ruby",5)
Roony = parrot("Roony",3)
print("Ruby is a {}".format(Ruby.species))
print("Roony is a {}".format(Roony.species))
print("{} is {} years old".format(Ruby.name,Ruby.age))
print("{} is {} years old".format(Roony.name,Roony.age))