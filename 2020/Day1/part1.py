with open('input.txt', 'r') as file:
    numbers = [int(i) for i in file.read().strip().split("\n")]

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                print(numbers[i] * numbers[j])
                exit()