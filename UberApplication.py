# This is where we can put the main code

# We should be able to check user logins and determine role off of userID 
# This will show a different menu and options based off of role

# Rider
# Menu Display
# - Map
# - Location
# - Request Ride button
# - End Ride button (if ride is active)
# - If ride is ended ping Rider for rating
# - Cancel Ride button (Only after ride is created)
# - View Rides button
# - View Profile button
# - Edit Profile button
# - Logout button

class Rider:
  def __init__(self, userID, name, email, phone, location):
    self.userID = userID
    self.name = name
    self.email = email
    self.phone = phone
    self.location = location
  def Login():
    #login
    pass
  def RequestRide():
    #request ride
    pass
  def RateDriver():
    #rate driver
    pass
  pass

class Driver:
  def __init__(self, driverID, name, vehicleID, locationID, status, rating):
    self.driverID = driverID
    self.name = name
    self.vehicleID = vehicleID
    self.locationID = locationID
    self.status = status
    self.rating = rating
  def AcceptRide():
    #accept ride
    pass
  def CompleteRide():
    #complete ride
    pass
  def UpdateLocation():
    #update driver location
    pass
  pass
class Ride:
  def __init__(self, rideID, status, startLocation, endLocation, fare, rider):
    self.rideID = rideID
    self.status = status
    self.startLocation = startLocation
    self.endLocation = endLocation
    self.fare = fare
    self.rider = rider
  def StartRide():
    #start ride
    pass
  def EndRide():
    #end ride
    pass
  pass

class Vehicle:
  def __init__(self, vehicleID, make, model, licensePlate):
    self.vehicleID = vehicleID
    self.make = make
    self.model = model
    self.licensePlate = licensePlate

class Location:
  def __init__(self, locationID, latitude, longitude, endLocation):
    self.locationID = locationID
    self.latitude = latitude
    self.longitude = longitude
    self.endLocation = endLocation
  def getAddress():
    #get address
    pass
  pass

class Payment:
  def __init__(self, paymentID, amount, timestamp, rider):
    self.paymentID = paymentID
    self.amount = amount
    self.timestamp = timestamp
    self.rider = rider
  def ProcessPayment():
    #process payment
    pass
  pass
    


# Driver
# - Map
# - When ride is requested ping Driver ride offer
# - When ride is accepted show map to user
# - If ride is cancelled ping Driver
# - When ride is ended ping Driver for rating
# - View Rides button
# - View Profile button
# - Edit Profile button
# - Logout button

# Admin 
# - Map
# - View Rides button
# - View Profile button
# - Edit Profile button
# - Logout button

# Once user is authenticated as rider/driver/admin menu will be displayed and status 
# will be set to 'active'
