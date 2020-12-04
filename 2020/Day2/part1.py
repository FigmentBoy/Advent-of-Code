with open('input.txt', 'r') as file:
    policies = [n.split(' ') for n in file.read().strip().split('\n')]
    count = 0
    for policy in policies:
        (low, high) = (int(n) for n in policy[0].split('-'))
        letter = policy[1][:1]
        string = policy[2]
    
        if low <= string.count(letter) <= high:
            count += 1

print(count)