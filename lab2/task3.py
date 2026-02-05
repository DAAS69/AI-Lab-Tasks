class Student:
  def __init__(self, name, student_id, marks):
    self.name = name
    self.student_id = student_id
    self.__marks = marks

  def get_marks(self):
    print(self.__marks)

  def set_marks(self, marks):
    self.__marks = marks
    print("marks updated")


  def calculate_grade(self):
    if self.__marks >= 90:
      print('A')
    elif self.__marks >= 80:
      print('B')
    elif self.__marks >= 70:
      print('C')
    elif self.__marks >= 60:
      print('D')
    else:
      print('F')



s1 = Student('Ali', 101, 85)
s2 = Student('Ahmed', 102, 92)

s1.calculate_grade()
s2.calculate_grade()

s1.set_marks(93)
s1.get_marks()
s1.calculate_grade()
