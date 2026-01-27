#Q1 student grading system
name = input("Please enter your name: ")
marks = int(input("Please enter your marks: "))

if marks >= 85:
  print(name)
  print("Your grade is A")
elif marks >= 70:
  print(name)
  print("your grade is B")

elif marks >= 50:
  print(name)
  print("Your grade is C")

elif marks <50:
  print(name)
  print("fail")
