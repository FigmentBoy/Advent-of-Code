total = 0
for line in open('input.txt', 'r'):
    sides = [int(i) for i in line.strip().split('x')]
    area = sides[0]*sides[1]*sides[2]

    small = [min(sides)]
    del sides[sides.index(small[0])]
    small.append(min(sides))

    total += sum(small) * 2 + area

print(total)