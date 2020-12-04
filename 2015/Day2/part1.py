total = 0
for line in open('input.txt', 'r'):
    x, y, z = (int(i) for i in line.strip().split('x'))

    sides = [x*y, y*z, x*z]
    add = min(sides)

    total += sum(sides) * 2 + add

print(total)