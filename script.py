student_number = int(input('Please enter the number of students in the class: '))
average = 0
total_grades = 0
max_grade = 0
students_info = []
passed_student = 0

# Collect student data
for i in range(student_number):
    student_name = input("Please enter student name: ")
    student_grade = float(input("Please enter student grade: "))
    
    average += student_grade
    students_info.append((student_name, student_grade))  #tuple

def get_heighest_grade(students_info):
    max_grade = students_info[0][1]
    for j in range(1, len(students_info)):
        if students_info[j][1] > max_grade:
            max_grade = students_info[j][1]
    return max_grade


# Display all students
def display_student_summary(students_info):
    for student in students_info:
        print("Student name:", student[0], "His mark is:", student[1])

#  average
def get_avg_grade(students_info):
    total = 0
    for student in students_info:
        total += student[1]
    return total / len(students_info)

# Count passed students
def count_passed(students_info):
    count = 0
    for student in students_info:
        if student[1] >= 60:
            count += 1
    return count


display_student_summary(students_info)
print("Average grade:", get_avg_grade(students_info))
print("Highest grade:", get_heighest_grade(students_info))

print("Number of students who passed:", count_passed(students_info))
