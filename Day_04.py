grid = [list(line.strip()) for line in open("text.txt","r")]

part1 = 0 
part2 = 0
target = "XMAS"

for i in range(len(grid)):
    for j in range(len(grid[0])):
            if j < len(grid[0]) - (len(target) - 1):
                string = "".join(grid[i][j:j+4])

                if target in {string,string[::-1]}:
                    part1 += 1

            if i < len(grid) - (len(target) - 1):
                if j < len(grid[0]) - (len(target) - 1):
                    string = "".join([grid[i+d][j+d] for d in range(len(target))])

                    if target in {string,string[::-1]}:
                        part1 += 1

                if j >= (len(target) - 1):
                    string = "".join([grid[i+d][j-d] for d in range(len(target))])
      
                    if target in {string,string[::-1]}:
                        part1 += 1
            if j < len(grid[0]) - (len(target) - 1):
                rotatedGrid = list(zip(*grid))
                string = "".join(rotatedGrid[i][j:j+4])

                if target in {string,string[::-1]}:
                    part1 += 1
            


target = "MAS"
for i in range(len(grid) - (len(target) - 1)):
    for j in range(len(grid[0]) - (len(target) - 1)):
        diagonal1 = "".join([grid[i+d][j+d] for d in range(len(target))])
        diagonal2 = "".join([grid[i+d][j+((len(target) - 1)-d)] for d in range(len(target))])

        if diagonal1 in {target,target[::-1]} and diagonal2 in {target,target[::-1]}:
            part2 += 1

print(part1,part2)
