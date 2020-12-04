with open('input.txt', 'r') as file:
    policies = [n.split(' ') for n in file.read().strip().split('\n')]
    count = 0
    for policy in policies:
        (pos1, pos2) = (int(n) - 1 for n in policy[0].split('-'))
        letter = policy[1][:1]
        string = policy[2]
    
        if (string[pos1] == letter) != (string[pos2] == letter): # XOR for chumps
            count += 1

print(count)