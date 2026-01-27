# Q2 even counter
num = int(input("Please enter the number: "))
count =0
for i in range(num):
  if(i%2==0):
    print(f'even number: {i}')
    count+=1

print(f'total number of even numbers were: {count}')
