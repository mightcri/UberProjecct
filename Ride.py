import uuid
class Ride():
  def __init__(self, riderID, startLocation, endLocation, startTime, endTime, fare, driverID = None):
    self.rideID = uuid.uuid4()
    self.riderID = riderID
    self.driverID = driverID
    self.startLocation = startLocation
    self.endLocation = endLocation
    self.startTime = startTime
    self.endTime = endTime
    self.status = "Inactive"
    self.duration = endTime - startTime
    self.fare = fare 

  def requestRide(self, riderID, driverID):
    # Here we will check if the rider and driver are available
    # if they are, we will return the rideID
    # if not, we will return None
    pass

  def rideAccepted(self, rideID, riderID, driverID):
    # Once ride is made then set riderID and driverID to 'unavailable'
    pass