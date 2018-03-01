
'''
Takes in filename as a string and returns array formatted as
per the description.
'''
def read_file(fname):
	if fname == "":
		fname = "a_example.in"
	file = open(fname, "r")
	line = file.readline()

	params = line.split(" ")
	rows = int(params[0])
	cols = int(params[1])
	cars = int(params[2])
	rides = int(params[3])
	bonus = int(params[4])
	steps = int(params[5])

	ride_list = []

	for i in range(rides):
		params = file.readline().split(" ")
		start_point = [int(params[0]), int(params[1])]
		end_point = [int(params[2]), int(params[3])]
		early_start = int(params[4])
		late_finish = int(params[5])
		ride_list.append([
			start_point[0], start_point[1], end_point[0], end_point[1],
			early_start, late_finish
		])

	file.close()
	return [rows, cols, cars, bonus, steps, ride_list]

'''
Takes in a name for the output file (will overwrite), and a list of lists
corresponding to each vehicles rides.
'''
def write_file(fname, vehicles):
	out_text = ""
	for v in vehicles:
		out_text += str(len(v))
		for i in range(len(v)):
			out_text += " "+str(v[i])
		out_text += "\n"
	out_file = open(fname, "wb")
	out_file.write(bytes(out_text, 'UTF-8'))
	out_file.close()
	return True

if __name__ == "__main__":
	write_file("test.out", [[0], [2,1]])

