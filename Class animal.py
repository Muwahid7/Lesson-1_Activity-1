from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can read and write")
class tiger(animal):
    def move(self):
        print("I can hunt fiercely")
class fish(animal):
    def move(self):
        print("I can swim")
class pigeon(animal):
    def move(self):
        print("I can fly")
R = human()
R.move()
R = tiger()
R.move()
R = fish()
R.move()
R = pigeon()
R.move()
