import uuid
from User import User
from Vehicle import Vehicle 
from Ride import Ride
# This is where we can put the main code

# We should be able to check user logins and determine role off of userID 
# This will show a different menu and options based off of role





# Admin 
# - Map
# - View Rides button
# - View Profile button
# - Edit Profile button
# - Logout button

# Once user is authenticated as rider/driver/admin menu will be displayed and status 
# will be set to 'active'

def main():
  # Here we will create the menu for the user to select from
  # Once the user has selected an option, the menu will be displayed again
  role = input('Please enter your role: ')
  username = input('Please enter username: ')
  password = input('Please enter password: ')
  role = role.capitalize()
  fName = input('Please Enter first name: ')
  fName = fName.capitalize()
  lName = input('Please Enter last name: ')
  lName = lName.capitalize()
  fullname = fName + ' ' + lName
  phone = list(input('Please Enter phone number: '))
  dash = 0
  phonestr = ''
  for i in phone:
    if dash == 3 or dash == 6:
      phonestr += '-'
    phonestr += str(i)
    dash += 1
  print(phonestr)

  email = input('Please Enter email: ')
  
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
  if role == 'Rider':
    # Make Rider object after checking role in case extra info is needed for driver/admin
    client = User(username, password, fullname, phonestr, email, role)
    print('Logging in...')
    print(client.login(username, password))
    choice = 1
    ridecreated = False
    while choice != 3:
      # checker for requesting ride vs cancelling ride in progress
      if ridecreated == False:
        print('Welcome ' + client.fullname)
        print('What would you like to do? ')
        print('1. Request Ride            2. Edit Profile')
        print('3. Close Application')
      elif ridecreated == True:
        print('Welcome ' + client.fullname)
        print('What would you like to do? ')
        print('1. Cancel Ride             2. Edit Profile')
        print('3. Close Application')
      # Main menu for Riders ^^ along with their choices vv
      choice = int(input('What would you like to do? '))
      while choice not in [1, 2, 3]:
        choice = int(input('Please enter a valid choice: '))
      if choice == 1:
        if ridecreated == False:
          print('You have selected to request a ride')
          ride, ridecreated = requestRide(client, ridecreated)
        elif ridecreated == True:
          fare = ride.fare
          ride = None
          print(f'Ride Cancelled. ${fare} has been refunded to your account.')
          ridecreated = False
      elif choice == 2:
        print('You have selected to edit your profile')
        print('1. Full Name            2. Phone Number')
        print('3. Email                4. Password')
        print('5. Role                 6. Return to Menu')
        choice = int(input('What would you like to edit? '))
        while choice not in [1,2,3,4,5,6]:
          print('1. Full Name            2. Phone Number')
          print('3. Email                4. Password')
          print('5. Role                 6. Return to Menu')
          choice = int(input('Please enter a valid choice: '))
        if choice == 1:
          fName = input('Please Enter first name: ')
          fName = fName.capitalize()
          lName = input('Please Enter last name: ')
          lName = lName.capitalize()
          fullname = fName + ' ' + lName
        elif choice == 2:
          phone = list(input('Please Enter phone number: '))
          print(phone)
          dash = 0
          phonestr = ''
          for i in phone:
            print(dash)
            if dash == 3 or dash == 6:
              phonestr += '-'
            phonestr += str(i)
            dash += 1
        elif choice == 3:
          email = input('Please Enter email: ')
        elif choice == 4:
          password = input('Please enter password: ')
        elif choice == 5:
          role = input('Please enter your role: ')
          role = role.capitalize()
        else:
          break
        client.edit_profile(username, password, fullname, phonestr, email, role)
        
    client.logout()
    print('Closing application...')
    exit()

  elif role == 'Driver':
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
    client = User(username, password, fullname, phonestr, email, role)    
    vehicle = client.addVehicle()
    print(vehicle)
    
    print('Logging in...')
    client.login(username, password)
    choice = 1
    rider = User('username', 'password', 'fullname', 'phonestr', 'email', 'Rider')
    ridecreated = False
    while choice != 3:
      if ridecreated == False:
        print('Welcome ' + client.fullname)
        print('What would you like to do? ')
        print('1. Edit Profile          2. View Profile')
        print('3. Logout')
        choice = int(input('What would you like to do? '))
        while choice not in [1,2,3]:
          print('1. Edit Profile           2. View Profile')
          print('3. Logout')
          choice = int(input('Please enter a valid choice: '))
        if choice == 1:
          print('You have selected to edit your profile')
          print('1. Full Name            2. Phone Number')
          print('3. Email                4. Password')
          print('5. Role                 6. Return to Menu')
          choice = int(input('What would you like to edit? '))
          while choice not in [1,2,3,4,5,6]:
            print('1. Full Name            2. Phone Number')
            print('3. Email                4. Password')
            print('5. Role                 6. Return to Menu')
            choice = int(input('Please enter a valid choice: '))
          if choice == 1:
            fName = input('Please Enter first name: ')
            fName = fName.capitalize()
            lName = input('Please Enter last name: ')
            lName = lName.capitalize()
            fullname = fName + ' ' + lName
          elif choice == 2:
            phone = list(input('Please Enter phone number: '))
            print(phone)
            dash = 0
            phonestr = ''
            for i in phone:
              print(dash)
              if dash == 3 or dash == 6:
                phonestr += '-'
              phonestr += str(i)
              dash += 1
          elif choice == 3:
            email = input('Please Enter email: ')
          elif choice == 4:
            password = input('Please enter password: ')
          elif choice == 5:
            role = input('Please enter your role: ')
            role = role.capitalize()
          else:
            break
          client.edit_profile(username, password, fullname, phonestr, email, role)
        elif choice == 2:
          print(client.fullname)
          print(client.phone)
          print(client.email)
          print(client.role)
        elif choice == 3:
          print('Closing application...')
          client.logout()
          exit()
        ride, ridecreated = requestRide(rider, ridecreated, client)
      else:
        print('Ride available')
        print(f'{rider.fullname}')
        print(f'{ride.startLocation} to {ride.endLocation}')
        print(f'${ride.fare}')
        print('What would you like to do? ')
        print('1. Accept Ride            2. View Profile')
        print('3. Logout')
        choice = int(input('What would you like to do? '))
        while choice not in [1,2,3,4]:
          print('1. Accept Ride            2. View Profile')
          print('3. Logout')
          choice = int(input('Please enter a valid choice: '))
        if choice == 1:
          acceptedRide = Ride(ride.riderID, ride.startLocation, ride.endLocation, 0, 0, ride.fare, client.driverID)
          client.status = 'unavailable'
          rider.status = 'unavailable'
          
        
          
      
      

def requestRide(client, ridecreated, driver = None, pickup = None, dropoff = None, distance = None):
  if pickup == None:
    pickup = input('Please enter the pickup location: ')
    dropoff = input('Please enter the dropoff location: ')
    distance = int(input(f'Please enter the distance between {pickup} and {dropoff}: '))
  fare = distance * 12
  print(f'The fare for your ride is ${fare}.00')
  pickup = pickup.capitalize()
  dropoff = dropoff.capitalize()
  if driver:
    driverID = driver.userid
  driverID = None
  riderid = client.userid
  ride = Ride(riderid, pickup, dropoff, 0, 0, fare, driverID)
  ridecreated = True
  return ride, ridecreated
  
if __name__ == "__main__":
  main()