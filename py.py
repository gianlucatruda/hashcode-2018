import vehicle
import ride

v = vehicle.vehicle()
r = ride.ride([0,0,1,3,2,9])

v.set_ride(r)
v.move()
