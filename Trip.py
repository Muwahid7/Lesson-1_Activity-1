hotel_cost_per_day = int(input("Enter the cost incurred per day"))
num_of_days = int(input("Enter the number of days stayed"))
plane_cost = int(input("Enter the flight cost"))
vehicle_cost = int(input("Enter the vehicle cost"))
total_hotel_cost = hotel_cost_per_day*num_of_days
total_cost = total_hotel_cost+plane_cost+vehicle_cost
print("The total cost of the trip is",total_cost)
 