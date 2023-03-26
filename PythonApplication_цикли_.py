
x = int(input('number_1: '))
y = int(input('number_2: '))
if x < y:
    x, y = y, x
for i in range(x, y+1):
    print(i)