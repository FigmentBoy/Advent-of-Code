matrix = [[True]]

def add_row(index: int=0):
    matrix.insert(index, [False] * len(matrix[0]))

def add_col(index: int=0):
    for row in matrix:
        row.insert(index, False)

x = y = 0
count = 1



for letter in open('input.txt', 'r').read().strip():
    if letter == "^":
        if y == 0:
            add_row(0)
        else:
            y -= 1;

    elif letter == "v":
        y += 1
        if y >= len(matrix):
            add_row(len(matrix))
    elif letter == "<":
        if x == 0:
            add_col(0)
        else:
            x -= 1
    elif letter == ">":
        x += 1
        if x >= len(matrix[0]):
            add_col(len(matrix[0]))

    if not matrix[y][x]:
        count += 1
        matrix[y][x] = True

print(count)