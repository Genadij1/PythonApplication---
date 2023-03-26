
x = int(input('num_1: '))
y = int(input('num_2: '))
for i in range(x, y+1):

    if i%3 == 0:
        print('Fizz')
    if i%5 == 0:
        print('Buzz')
    if i%3 == 0 and i%5 == 0:
        print("Fizz Buzz")
    if i%3 != 0 and i%5 != 0:
        print(i)