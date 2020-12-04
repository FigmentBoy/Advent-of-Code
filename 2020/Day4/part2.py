CONFIG = {
    "REQUIRED": {
        "byr": lambda i: len(i) == 4 and 1920 <= int(i) <= 2002, 
        "iyr": lambda i: len(i) == 4 and 2010 <= int(i) <= 2020, 
        "eyr": lambda i: len(i) == 4 and 2020 <= int(i) <= 2030,
        "hgt": lambda i: 150 <= int(i[:-2]) <= 193 if i.endswith("cm") else 59 <= int(i[:-2]) <= 76 if i.endswith("in") else False, 
        "hcl": lambda i: i[0] == "#" and set(i[1:]) <= set("0123456789abcdef"),
        "ecl": lambda i: i in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], 
        "pid": lambda i: len(i) == 9
    },
    "OPTIONAL": [
        "cid"
    ]
}

count = 0
with open('input.txt', 'r') as file:
    pps = [n.replace("\n", " ") for n in file.read().strip().split('\n\n')]
    for i in range(len(pps)):
        pps[i] = [s.split(':') for s in pps[i].split(' ')]
        pp = {}

        for z in [{k: v} for [k, v] in pps[i]]:
            pp.update(z)
        
        for key in CONFIG["REQUIRED"].keys():
            if key not in pp.keys():
                break
            elif CONFIG["REQUIRED"][key](pp[key]):
                pass
            else:
                print(key, pp[key], "INVALID")
                break
        else:
            count += 1

print(count)
