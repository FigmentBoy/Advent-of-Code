matrix = []
for line in open('input.txt', 'r'):
    matrix.append([l for l in line.strip()])

trees = 0

for i, x in enumerate(matrix):
    if x[int(i*3) % (len(x))] == "#":
        trees += 1

print(trees)