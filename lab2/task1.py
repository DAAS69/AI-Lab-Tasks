class Vehicle:
  def __init__(self,name, vehicle_id, brand, rent_per_day):
    self.name = name
    self.vehicle_id = vehicle_id
    self.brand = brand
    self.rent_per_day = rent_per_day

  def display_details(self):
    print(f'Name: {self.name} \nVehicle id: {self.vehicle_id} \nBrand: {self.brand} \nRent per day: {self.rent_per_day}')

  def calculate_rent(self,days):
    print(f'rent is: {self.rent_per_day * days}')


 
car1 = Vehicle('corolla', 101, 'Toyota', 5000)
car2 = Vehicle('civic', 102, 'Honda', 2000)
    
car1.display_details()
car2.display_details()

car1.calculate_rent(5)
car2.calculate_rent(3)


