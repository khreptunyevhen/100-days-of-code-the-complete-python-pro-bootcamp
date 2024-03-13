heights = input("Please enter the student hights separate by space:\n")
student_heights = heights.split()

number_students = len(student_heights)
total_height = 0
highest_student = 0

for index in range(0, len(student_heights)):
	student_heights[index] = int(student_heights[index])
	total_height += student_heights[index]
	if student_heights[index] > highest_student:
		highest_student = student_heights[index]

average_height = total_height / number_students

print(f"Total height: {total_height}")
print(f"Total students: {number_students}")
print(f"Average height: {average_height}")
print(f"Highest student: {highest_student}")