# Q3 dictionary question
student_records = {}

for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    student_records[name] = marks

print("Student Records:")
for name in student_records:
    marks = student_records[name]
    print(f'{name} : {marks}')
