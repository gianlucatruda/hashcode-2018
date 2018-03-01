import sys
import ride



def can_finish(v, r, t):
    d = v.distance([r.data[0], r.data[1]], [r.data[2], r.data[3]])
    if v.distance([r.data[0], r.data[1]], v.curr_pos) + d < r.data[5]:
        return d
    else:
        return -1

def assign(vehicles, rides, curr_time):
    for v in vehicles:
        allAssigned = True
        if v.ttl != 0:
            continue


        max_dist = -10000000000
        max_dist_ride = ride.ride([0,0,0,0,0,0])
        max_dist_ind = 0
        # min_dist = sys.maxsize
        # min_dist_ride = ride.ride([0,0,0,0,0,0])
        # min_dist_ind = 0
        actually = False
        for ind, r in enumerate(rides):
                # find closes ride
            if not r.assigned:
                dist = v.distance([r.data[0], r.data[1]], v.curr_pos)

                dis = can_finish(v, r, curr_time)
                if dis != -1:
                    if dis > max_dist:
                        actually = True
                        max_dist = dis
                        max_dist_ride = r
                        max_dist_ind = ind

                # if dist < min_dist:
                #     min_dist = dist
                #     min_dist_ride = r
                #     min_dist_ind = ind
                #     actually = True

                allAssigned = False
        if actually:
            v.set_ride(max_dist_ride, curr_time, max_dist_ind )
            max_dist_ride.assign()
        # rides = map(lambda x: not x.assigned, rides)
        if allAssigned: break
