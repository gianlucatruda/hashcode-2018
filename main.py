import hash_io as io
import scheduler
import vehicle
import ride

file_names = [
	"a_example",
	"b_should_be_easy",
	"c_no_hurry",
	"d_metropolis",
	"e_high_bonus"
]

for f in file_names:
	print("Reading:",f)
	params = io.read_file(f+".in")
	# [rows, cols, cars, bonus, steps, ride_list]

	dimensions = [params[0], params[1]]
	num_cars = params[2]
	bonus = params[3]
	num_steps = params[4]

	ride_list = params[5]
	# [start_point_x, start_point_y, end_point_x, end_point_y, early_start, late_finish]

	vehicles = []
	rides = []

	for i in range(num_cars):
		vehicles.append(vehicle.vehicle())

	for l in ride_list:
		rides.append(ride.ride(l))

	for i in range (num_steps):
		if ((100*i)/num_steps)%5 == 0:
			print(str((100*i)/num_steps)+"%",end="\r")
		scheduler.assign(vehicles, rides, i)
		for v in vehicles:
			v.move()

	io.write_file(f+".out", vehicles)
	print("Finished:",f)
