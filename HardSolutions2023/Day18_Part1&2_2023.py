import re

instructions = [line.strip() for line in open("text.txt","r")]

RL = "RL"
UD = "UD"

def add(t1,t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

clockwiseTurns = "RDLUR"

def findLoopArea(pInstructions):
    pos = (0,0)
    points = []
    edgeSum = 0
    cornerSum = 0
    for i in range(len(pInstructions) - 1):
        direction, distance = pInstructions[i]
        nextDirection, _ = pInstructions[i+1]
        if direction in RL:
            pos = add(pos, ((2*RL.find(direction) - 1) * distance,0))
        else:
            pos = add(pos, (0,(2*UD.find(direction) - 1) * distance))

        points.append(pos)
        edgeSum += distance - 1
        cornerSum += 3 if direction + nextDirection in clockwiseTurns else 1
    
    points += [points[0]]
    areaBetweenPoints = 0
    for i in range(len(points) - 1):
        areaBetweenPoints += (1/2) * (points[i][1] + points[i+1][1])*(points[i][0] - points[i+1][0])

    res = abs(areaBetweenPoints) + edgeSum/2 + cornerSum/4
    return int(res)

part1Instructions = []
part2Instructions = []

instructions += [instructions[0]]

for i in range(len(instructions)):
    line = instructions[i]

    part1Direction, part1Distance = re.findall(r'(\S{1}) *(\d+)', line)[0]
    part1Distance = int(part1Distance)
    part1Instructions.append((part1Direction, part1Distance))

    part2Instruction = re.findall(r'\(\#*(\S{6})\)', line)[0]
    part2Direction = clockwiseTurns[int(part2Instruction[-1])]
    part2Distance = int(part2Instruction[:-1],16)
    
    part2Instructions.append((part2Direction, part2Distance))


print(f"Part 1: {findLoopArea(part1Instructions)}, Part 2: {findLoopArea(part2Instructions)}.")
