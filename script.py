student_number = int(input('Please enter the number of students in the class: '))
students_info = []

for i in range(student_number):
    student_name = input("Please enter student name: ")
    student_grade = float(input("Please enter student grade: "))
    students_info.append([student_name, student_grade])

def get_highest_grade(students_info):
    max_grade = students_info[0][1]
    for student in students_info[1:]:
        if student[1] > max_grade:
            max_grade = student[1]
    return max_grade

def display_student_summary(students_info):
    for student in students_info:
        print("Student name:", student[0], "His mark is:", student[1])

def get_avg_grade(students_info):
    total = 0
    for student in students_info:
        total += student[1]
    return total / len(students_info)

def count_passed(students_info):
    count = 0
    for student in students_info:
        if student[1] >= 60:
            count += 1
    return count

print("Highest grade:", get_highest_grade(students_info))
display_student_summary(students_info)
print("Average grade:", get_avg_grade(students_info))
print("Number of students who passed:", count_passed(students_info))
