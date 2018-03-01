import hash_io as io
import scheduler
import vehicle
import ride

params = io.read_file("b_should_be_easy.in")
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
# The meat
for i in range (num_steps):
	scheduler.assign(vehicles, rides, i)
	for v in vehicles:
		v.move()

io.write_file("b_should_be_easy.out", vehicles)
