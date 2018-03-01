import sys
import ride



def can_finish(v, r, t):
    snd = v.distance([r.data[0], r.data[1]], [r.data[2], r.data[3]])
    fst =v.distance([r.data[0], r.data[1]], v.curr_pos)

    if  fst + snd< r.data[5]:
        return [fst, snd]
    else:
        return [-1, -1]

def assign(vehicles, rides, curr_time):
    for v in vehicles:
        allAssigned = True
        if v.ttl != 0:
            continue


        max_dist = -10000000000
        max_dist_ride = ride.ride([0,0,0,0,0,0])
        max_dist_ind = 0
        pos_max = max_dist
        pos_max_ride = max_dist_ride
        pos_max_ind = 0
        pos_set = False
        # min_dist = sys.maxsize
        # min_dist_ride = ride.ride([0,0,0,0,0,0])
        # min_dist_ind = 0
        actually = False
        for ind, r in enumerate(rides):
                # find closes ride
            if not r.assigned:
                dist = v.distance([r.data[0], r.data[1]], v.curr_pos)

                dis = can_finish(v, r, curr_time)
                if dis[0] != -1:
                    if r.data[4] == dis[1] + curr_time:
                        if dis[1] > pos_max:
                            pos_set = True
                            pos_max = dis[1]
                            pos_max_ind = ind
                            pos_max_ride = r
                    if dis[1] > max_dist:
                        actually = True
                        max_dist = dis[1]
                        max_dist_ride = r
                        max_dist_ind = ind



                allAssigned = False
        if pos_set:
            v.set_ride(pos_max_ride, curr_time, pos_max_ind )
            pos_max_ride.assign()
        elif actually:
            v.set_ride(max_dist_ride, curr_time, max_dist_ind )
            max_dist_ride.assign()
        # rides = map(lambda x: not x.assigned, rides)
        if allAssigned: break
