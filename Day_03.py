line = "".join([line.strip()for line in open("text.txt","r")])

part1 = 0 
part2 = 0

i = 0
search = True

while i < len(line):

    if line[i:i+4] == "do()":
        search = True
        i += 4
    if line[i:i+7] == "don't()":
        search = False
        i += 7
        
    if line[i:i+4] == "mul(":
        i += 4
        num = ""
        while line[i].isdigit():
            num += line[i]
            i += 1

        if line[i] == "," and len(num) > 0:
            i += 1
            num2 = ""
            while line[i].isdigit():
                num2 += line[i]
                i += 1

            if line[i] == ")" and len(num2) > 0:
                multiplication = int(num) * int(num2)
                part1 += multiplication
                if search:
                    part2 += multiplication

    i += 1

print(f"Part 1: {part1}, Part 2: {part2}")
