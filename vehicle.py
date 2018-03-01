import ride
import math

class vehicle:
    ttl = 0
    curr = ride.ride([0,0,0,0,0,0])
    curr_pos =[0,0]
    rides = []

    def move(self):
        self.ttl -= 1

    def set_ride(self, ride, time, ride_index):
        # ttl = dist to pickup + (ES- ( time + dist) ) + dist to drop
        self.curr_pos = [self.curr.data[2], self.curr.data[3]]
        self.rides.append(ride_index)

        self.curr = ride

        dist1 = self.distance(self.curr_pos, [ride.data[0], ride.data[1]])
        dist2 = self.distance([ride.data[0], ride.data[1]], [ride.data[2], ride.data[3]])

        self.ttl = dist1 + max(ride.data[4] - time + dist1,0) + dist2

    def distance(self, c, d):
        return math.fabs(d[0] - c[0]) + math.fabs (d[1] - c[1])
