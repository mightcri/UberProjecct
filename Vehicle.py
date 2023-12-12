import uuid
class Vehicle():
  def __init__(self, driverID, licensePlate, make, model, color, year, seats):
    self.vehicleID = uuid.uuid4() #ID to be linked to user
    self.driverID = driverID
    self.licensePlate = licensePlate
    self.make = make
    self.model = model
    self.color = color
    self.year = year
    self.seats = seats
    self.status = "Offline"

# Starting and ending shifts
  def startShift(self):
    self.status = "Available"
    return
    
  def endShift(self):
    # Switches Status to Offline
    self.status = "Offline"

  def editVehicle(self, licensePlate, make, model, color, year, seats):
    # The user will input information and the program will call this method to update the vehicle
    self.licensePlate = licensePlate
    self.make = make
    self.model = model
    self.color = color
    self.year = year
    self.seats = seats
    
    