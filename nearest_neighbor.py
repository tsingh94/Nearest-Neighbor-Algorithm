import sys
import time

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


def brute_Force_Algo(all_Points):
	
	time_Start = time.time()

	smallest_Dist = float("inf")

	for i in range(0,len(all_Points)):
		
		for j in range((i+1),len(all_Points)):
		
			diff_X = all_Points[i][0] - all_Points[j][0]  
			diff_Y = all_Points[i][1] - all_Points[j][1] 
			distance = (diff_X**(2) + diff_Y**(2))**(.5)

			if distance < smallest_Dist:
				smallest_Dist = distance

	time_Stop = time.time()
	print("Execution Time: ", time_Stop - time_Start)

	filename  = str(sys.argv[1])
	file_Writer = open(filename[:len(filename)-4] + "_distance.txt", "w")
	file_Writer.write(str(smallest_Dist))
	file_Writer.close()

	#print("Smallest Distance is : ", smallest_Dist)


def find_Smallest_Pair(points):
	
	print(points)
	print("\n")
	print (len(points))
	print("\n")

	if len(points) == 2 or len(points) == 3:
		#diff_X = points[0][0] - points[1][0]
		#diff_Y = points[0][1] - points[1][1]
		#return (diff_X**(2) + diff_Y**(2))**(.5)
		return brute_Force_Algo(points)

	if len(points) % 2 == 0:
		return max (find_Smallest_Pair(points[:int((len(points)/2))]), find_Smallest_Pair(points[int((len(points)/2)):]))

	else:
		num1 = find_Smallest_Pair(points[:int(((len(points)-1)/2)+1)])
		num2 = find_Smallest_Pair(points[int(((len(points)-1)/2)+1):])

		print("num1: ", num1)
		print("\n")
		print("num2: ", num2)
		print("\n")




def faster_Algo(all_Points):
	
	points_Sorted_By_X = sorted(all_Points, key = lambda coordinate: coordinate[0])
	points_Sorted_By_Y = sorted(all_Points, key = lambda coordinate: coordinate[1])

	print (find_Smallest_Pair(points_Sorted_By_X))
	#print (all_Points)
	#print ("\n")
	#print(points_Sorted_By_X)
	#print ("\n")
	#print (points_Sorted_By_Y)
	#print ("\n")



all_Points = get_All_Points()
#faster_Algo(all_Points)
brute_Force_Algo(all_Points)



