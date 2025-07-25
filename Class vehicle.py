class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
ob = vehicle(398,39)
print("Max spped is",ob.max_speed)
print("Mileage is",ob.mileage)