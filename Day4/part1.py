CONFIG = {
    "REQUIRED": [
        "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
    ],
    "OPTIONAL": [
        "cid"
    ]
}

count = 0
with open('input.txt', 'r') as file:
    pps = [n.replace("\n", " ") for n in file.read().split('\n\n')]
    for i in range(len(pps)):
        pps[i] = [s.split(':') for s in pps[i].split(' ')]
        pp = {}

        for z in [{k: v} for [k, v] in pps[i]]:
            pp.update(z)
        
        for key in CONFIG["REQUIRED"]:
            if key not in pp.keys():
                break
        else:
            count += 1

print(count)