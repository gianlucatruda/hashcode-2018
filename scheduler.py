def assign(vehicles, rides, curr_time):
	for i in range(len(rides)):
		if i>len(vehicles)-1:
			break
		if not rides[i].assigned:
			vehicles[i].set_ride(rides[i], curr_time, i)
			rides[i].assigned = True

