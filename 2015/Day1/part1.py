floor = 0
for letter in open('input.txt', 'r').read().strip():
    if letter == "(":
        floor += 1
    elif letter == ")":
        floor -= 1

print(floor)