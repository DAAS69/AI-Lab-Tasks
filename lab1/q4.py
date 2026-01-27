# Q4 menu

def add(num1,num2):
  return num1 + num2

def subtract(num1,num2):
  return num1 - num2
print("""
1. add two numbers
2. subtract two numbers
3. exit
""")
key = int(input("Please enter your choice: "))
while key != 3:
  if key == 1:
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number: "))
    print(f'The result is: {add(num1,num2)}')
  elif key == 2:
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number: "))
    print(f'The result is: {subtract(num1,num2)}')

  key = int(input("Please enter your choice: "))

print("Exiting program")
