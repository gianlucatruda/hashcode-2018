import sys
import ride
def assign(vehicles, rides, curr_time):
    for v in vehicles:
        allAssigned = True
        if v.ttl != 0:
            continue
        min_dist = sys.maxsize
        min_dist_ride = ride.ride([0,0,0,0,0,0])
        min_dist_ind = 0
        actually = False
        for ind, r in enumerate(rides):
                # find closes ride
            if not r.assigned:
                dist = v.distance([r.data[0], r.data[1]], v.curr_pos)
                if dist < min_dist:
                    min_dist = dist
                    min_dist_ride = r
                    min_dist_ind = ind
                    actually = True

                allAssigned = False
        if actually:
            v.set_ride(min_dist_ride, curr_time, min_dist_ind )
            min_dist_ride.assign()
        # rides = map(lambda x: not x.assigned, rides)
        if allAssigned: break
