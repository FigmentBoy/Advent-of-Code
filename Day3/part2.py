matrix = []
for line in open('input.txt', 'r'):
    matrix.append([l for l in line.strip()])

slopes = [1, 3, 5, 7, 1/2]

trees = []

for z, s in enumerate(slopes):
    trees.append(0)
    for i, x in enumerate(matrix):
        if type(i*s) == float and not (i*s).is_integer():
            pass
        elif x[int(i*s) % (len(x))] == "#":
            trees[z] += 1

s = 1;
for t in trees:
    s *= t;
print(trees, s)