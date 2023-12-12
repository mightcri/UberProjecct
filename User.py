import uuid
from Vehicle import Vehicle
class User():
  #class created when first signup
  def __init__(self, username, password, fullname, email, phone, role):
    #userid needs to be unique and only recognizable by pc
    # username, password, fullname, email, phone, role
    self.username = username
    self.password = password
    self.fullname = fullname
    self.email = email
    self.phone = phone
    self.role = role
    self.vehicleID = None #vehicleID to be matched to user
    self.status = "active"
    self.ratings = {} # keys: rating, values: comments
    self.userid = uuid.uuid4()
    
  #used when user logs in
  def login(self, username, password):
    if self.username == username and self.password == password:
      return True
    else:
      return False
  
  #class created when user logs out
  def logout(self):
    self.status = "inactive"
    return
    
  
  def edit_profile(self, username, password, fullname, email, phone, role):
    self.username = username
    self.password = password
    self.fullname = fullname
    self.email = email
    self.phone = phone
    self.role = role
    return

  # These methods are for Drivers ONLY 
  def acceptRide(self, userID, rideID):
    # Here the user can accept a ride
    pass
  def declineRide(self, userID, rideID):
    # Here the user can decline a ride
    pass
  def cancelRide(self, userID, rideID):
    # Here the user can cancel a ride
    pass
  def endRide(self, userID, rideID):
    # Here the user can end a ride
    pass
  def addVehicle(self):
    plate = input("Enter vehicle plate number: ")
    make = input('What is the vehicles make? ')
    make = make.capitalize()
    model = input('What is the vehicles model? ')
    model = model.capitalize()
    color = input('What is the vehicles color? ')
    color = color.capitalize()
    year = input('What is the vehicles year? ')
    seats = input('How many seats does the vehicle have? ')
    id = uuid.uuid4()
    vehicle = Vehicle(self.userid, plate, make, model, color, year, seats)
    self.vehicleID = vehicle.vehicleID
    return vehicle
  def userRole(self, userID):
    # Here the method will take in the userID and return the role of the user for user menu in main
    pass

  def rideRating(self, rideID, otherID):
    rating = int(input('What is your rating for this ride? '))
    while rating > 5 or rating < 1:
      rating = int(input('Please enter a valid rating (1-5): '))
    return rating