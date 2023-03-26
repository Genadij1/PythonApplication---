
x = int(input('num_1: '))
y = int(input('num_2: '))
for i in range(x, y+1):
     if i%3 == 0 and i%5 == 0:
           print("Fizz Buzz")
     elif i%3 == 0:
           print("Fizz")
     elif i%5 == 0:
           print("Buzz")
     else:
           print(i)