# Q5 list of marks

def calculate_average(num):
  sum = 0
  count = 0
  for i in num:
      sum += i
      count +=1
  average = sum/count
  return average

marks = [70,80,90]
average = calculate_average(marks)
print(f'marks: {marks}')
print(f'average marks: {average}')
