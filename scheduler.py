def assign(vehicles, rides, curr_time):
	for v in vehicles:
		allAssigned = True
		for ind, r in enumerate(rides):
			if not r.assigned:
				allAssigned = False
				if v.ttl != 0:	continue
				v.set_ride(r, curr_time, ind )
				r.assign()
		if allAssigned: break
