import hash_io as io
import vehicle
import ride

params = io.read_file("b_should_be_easy.in")
# [rows, cols, cars, bonus, steps, ride_list]

dimensions = [params[0], params[1]]
num_cars = params[2]
bonus = params[3]
num_steps = params[4]

ride_list = params[5]
# [i, start_point, end_point, early_start, late_finish]

vehicles = []
rides = []

for i in range(num_cars):
	vehicles.append(vehicle())

for i in range(len(ride_list)):
	rides.append(ride(ride_list[i]))

for i in range num_steps:
	for v in vehicles:
		# check rides

