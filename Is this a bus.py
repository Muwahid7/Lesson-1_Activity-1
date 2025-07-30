class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed =  max_speed
        self.mileage = mileage
class bus(vehicle):
    pass
school_bus = bus("school volvo",68,23)
print("Name of the School bus",school_bus.name)
print("The max speed of the bus is",school_bus.max_speed)
print("The mileage of the bus is",school_bus.mileage)