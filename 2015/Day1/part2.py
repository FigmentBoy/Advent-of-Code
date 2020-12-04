floor = 0
for i, letter in enumerate(open('input.txt', 'r').read().strip()):
    if letter == "(":
        floor += 1
    elif letter == ")":
        floor -= 1

    if floor < 0:
        print(i + 1)
        exit()

