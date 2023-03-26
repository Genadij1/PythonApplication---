
x = int(input('num_1: '))
y = int(input('num_2: '))
for i in range(x, y+1):
    print(i)
print()
for i in range(y, x-1, -1):
    print(i)
print()
for i in range(x, y+1):
    if i%7 == 0:
        print(i)
print()
c = 0
for i in range(x, y+1):
    if i%5 == 0:
        c += 1
        print(c)