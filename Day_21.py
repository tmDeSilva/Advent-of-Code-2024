from collections import Counter

dirs = [(1,0), (0,1), (-1,0), (0,-1)]
dirChars = ">v<^"
dirDict = dict(zip(dirs, dirChars))
dirCharDict = dict(zip(dirChars, dirs))
dirDict[(0,0)] = "#"

padsString = """
789
456
123
#0A

#^A
<v>
"""[1:].split("\n\n")

numericPadString, arrowPadString = padsString

numericPad = [line.strip() for line in numericPadString.split()]
arrowPad = [line.strip() for line in arrowPadString.split()]

def getPos(pChar,pGrid):
    for i in range(len(pGrid)):
        for j in range(len(pGrid[0])):

            if pGrid[i][j] == pChar:
                return((j,i))
            
    return (-1,-1)

def getSign(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1

def getRoute(pPair, pGrid):

    start,final = pPair
    sx, sy = getPos(start, pGrid)
    fx, fy = getPos(final, pGrid)

    dx, dy = fx - sx, fy - sy
    hString = dirDict[(getSign(dx),0)] * abs(dx)
    vString = dirDict[(0,getSign(dy))] * abs(dy)

    if dx > 0 and pGrid[fy][sx] != "#":
        return vString + hString + "A"
    if pGrid[sy][fx] != "#":
        return hString + vString + "A"
    if pGrid[fy][sx] != "#":
        return vString + hString + "A"
    
memo = {}

numberPadChars = "".join([str(i) for i in range(10)]) + "A"
arrPadChars = dirChars + "A"

for i in range(len(numberPadChars)):
    for j in range(len(numberPadChars)):
        iPair = numberPadChars[i] + numberPadChars[j]
        memo[iPair] = getRoute(iPair, numericPad)

for i in range(len(arrPadChars)):
    for j in range(len(arrPadChars)):
        iPair = arrPadChars[i] + arrPadChars[j]
        memo[iPair] = getRoute(iPair, arrowPad)

part1 = 0
part2 = 0

part1SubControls = 2
part2SubControls = 25

for line in open("text.txt","r").readlines():
    toPress = Counter([line.strip()])
    number = int(line.strip()[:-1])

    for iteration in range(part2SubControls + 1):
        nToPress = Counter()
        for sButtons, instances in toPress.items():
            sButtons = "A" + sButtons
            newCoder = Counter([memo[sButtons[i] + sButtons[i+1]] for i in range(len(sButtons) - 1)])
            for iSeq in newCoder:
                newCoder[iSeq] *= instances
            nToPress.update(newCoder)

        if iteration == part1SubControls + 1:
            part1 += sum([len(iSeq) * instances for iSeq,instances in toPress.items()]) * number 

        toPress = nToPress
        
    part2 += sum([len(iSeq) * instances for iSeq,instances in toPress.items()]) * number

print(f"Part 1: {part1}, Part 2: {part2}.")
