def assign(vehicles, rides, curr_time)

for i in range(len(rides)):
	vehicles[i].set_ride(rides[i], curr_time, i)

