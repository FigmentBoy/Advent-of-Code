matrix = [[True]]

def add_row(index: int=0):
    matrix.insert(index, [False] * len(matrix[0]))

def add_col(index: int=0):
    for row in matrix:
        row.insert(index, False)

santa = [0, 0]
robo = [0, 0]

count = 1


for i, letter in enumerate(open('input.txt', 'r').read().strip()):
    which = i % 2 == 0

    if letter == "^":
        if which and robo[1] == 0:
            add_row(0)
            santa[1] += 1
        elif not which and santa[1] == 0:
            add_row(0)
            robo[1] += 1
        elif which:
            robo[1] -= 1
        else:
            santa[1] -= 1
            
    elif letter == "v":
        if which:
            robo[1] += 1
        else:
            santa[1] += 1

        if which and robo[1] >= len(matrix):
            add_row(len(matrix))
        elif not which and santa[1] >= len(matrix):
            add_row(len(matrix))

    elif letter == "<":
        if which and robo[0] == 0:
            add_col(0)
            santa[0] += 1
        elif not which and santa[0] == 0:
            add_col(0)
            robo[0] += 1
        elif which:
            robo[0] -= 1
        else:
            santa[0] -= 1
    elif letter == ">":
        if which:
            robo[0] += 1
        else:
            santa[0] += 1

        if which and robo[0] >= len(matrix[0]):
            add_col(len(matrix[0]))
        elif not which and santa[0] >= len(matrix[0]):
            add_col(len(matrix[0]))

    if which and not matrix[robo[1]][robo[0]]:
        count += 1
        matrix[robo[1]][robo[0]] = True

    elif not which and not matrix[santa[1]][santa[0]]:
        count += 1
        matrix[santa[1]][santa[0]] = True


print(count)