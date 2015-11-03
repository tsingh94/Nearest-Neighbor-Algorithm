import sys
import time

# this function will read all of the points 
# from the file and populate a list of tuples.
# each tuple is one point with x and y coordinate
def get_All_Points():
	
	points = []
	
	filename  = str(sys.argv[1])
	file_reader = open(filename, "r")

	for i in file_reader:
		single_row = i.split()
		coordinate = (float(single_row[0]), float(single_row[1]))
		points.append(coordinate);

	file_reader.close()

	return points; 

# this function runs the brute force algorithm for the closest pair.
# it will return the smallest distance between any 2 points
def brute_Force_Algo(all_Points):
	
	smallest_Dist = float("inf")

	for i in range(0,len(all_Points)):
		
		for j in range((i+1),len(all_Points)):
		
			# calculating Euclidean distance between 2 points 
			diff_X = all_Points[i][0] - all_Points[j][0]  
			diff_Y = all_Points[i][1] - all_Points[j][1] 
			distance = (diff_X**(2) + diff_Y**(2))**(.5)

			if distance < smallest_Dist:
				smallest_Dist = distance

	return smallest_Dist

	
# this function calculates the distances which have one point on the
# left side and one point on the right in the appropriate strip.
# returns the smallest distance in the strip
def find_Min_In_Strip(points_Sorted_By_Y, d, median):
	
	new_Point_List = []

	# removing all points that are not in the strip outlined by d
	for i in range(0, len(points_Sorted_By_Y)):
		
		curr_Point = points_Sorted_By_Y[i][0]
		 
		if not((curr_Point > (median + d)) or (curr_Point < (median - d))):
			new_Point_List.append(points_Sorted_By_Y[i])

	
	# calculating the smallest distance among the remaining points 
	for i in range(0, len(new_Point_List)):
		j = 1
		#comparing an element with the next 7 elements next to it
		while(((i + j) < len(new_Point_List)) and (j < 8)):
			diff_X = new_Point_List[i][0] - new_Point_List[i+j][0]  
			diff_Y = new_Point_List[i][1] - new_Point_List[i+j][1] 
			distance = (diff_X**(2) + diff_Y**(2))**(.5)

			if (distance < d):
				distance = d
			
			j = j + 1

	return d

# this function is the main divide and conquer algorithm
# this function calls the find_Min_In_Strip function
# takes in all of the points that need to be compared and
# returns the smallest distance
def find_Smallest_Pair(points):
	
	if len(points) == 2 or len(points) == 3:
		return brute_Force_Algo(points)

	if len(points) % 2 == 0:
		num1 = find_Smallest_Pair(points[:int((len(points)/2)+1)]) 
		num2 = find_Smallest_Pair(points[int((len(points)/2)):])
		d =  min(num1, num2)

	else:
		num1 = find_Smallest_Pair(points[:int(((len(points)-1)/2)+1)])
		num2 = find_Smallest_Pair(points[int(((len(points)-1)/2)):])
		d =  min(num1, num2)

	if len(points) % 2 == 0:
		median = (len(points)/2) + 1


	else:
		median = points[int((len(points) + 1)/2)][0]
	
	points_Sorted_By_Y = sorted(points, key = lambda coordinate: coordinate[1])

	return find_Min_In_Strip(points_Sorted_By_Y, d, median)


# this function does some initializations for the divide and conquer algorithm to run
# calls the find_Smallest_Pair function and returns the smallest distance
def faster_Algo(all_Points):
	
	points_Sorted_By_X = sorted(all_Points, key = lambda coordinate: coordinate[0])
	
	return find_Smallest_Pair(points_Sorted_By_X)

# getting all of the points from the file
all_Points = get_All_Points()

time_Start = time.time()

smallest_Dist_Faster_Algo = faster_Algo(all_Points)

time_Stop = time.time()

print("Execution Time for Divide and Conquer Algorithm (secs): ", time_Stop - time_Start)

time_Start = time.time()

smallest_Dist_Brute_Force = brute_Force_Algo(all_Points)

time_Stop = time.time()

print("Execution Time for Brute Force Algorithm (secs): ", time_Stop - time_Start)

#writing to the file
filename  = str(sys.argv[1])
file_Writer = open(filename[:len(filename)-4] + "_distance.txt", "w")
file_Writer.write("Distance of closest pair calculated by divide and conquer algorithm: ")
file_Writer.write(str(smallest_Dist_Faster_Algo))
file_Writer.write("\nDistance of closest pair calculated by brute force algorithm: ")
file_Writer.write(str(smallest_Dist_Brute_Force))
file_Writer.close()


