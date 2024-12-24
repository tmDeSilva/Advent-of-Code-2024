grid = [list(line.strip()) for line in open("text.txt","r").readlines()]
freqs = {}
#For debugging
def display():
    for line in grid:
        print("".join(line))
    input()
    
def isInGrid(pPoint):
    return (0 <= pPoint[0] < len(grid[0]) and 0 <= pPoint[1] < len(grid))

#Vector calcs
def subtracter(t1,t2):
    return (t1[0]-t2[0], t1[1] - t2[1])

def adder(t1,t2):
    return (t1[0]+t2[0], t1[1] + t2[1])


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '.':
            try:
                freqs[grid[i][j]].append((j,i))
            except:

                freqs[grid[i][j]] = [(j,i)]

part1Antinodes = set()
for freq in freqs.keys():
    L = freqs[freq]

    for a in range(len(L)-1):
        for b in range(a+1,len(L)):

            antinode1 = adder(L[a],subtracter(L[a],L[b]))
            antinode2 = adder(L[b],subtracter(L[b],L[a]))
            if isInGrid(antinode1):
                part1Antinodes |= {antinode1}
            if isInGrid(antinode2):
                part1Antinodes |= {antinode2}


part1 = len(part1Antinodes)

part2Antinodes = set()
for freq in freqs.keys():
    L = freqs[freq]
    part2Antinodes |= set(L)
    for a in range(len(L)-1):
        for b in range(a+1,len(L)):
            va = subtracter(L[a],L[b])
            vb = subtracter(L[b],L[a])

            currentNode = adder(L[a],va)
  
            while isInGrid(currentNode):
                part2Antinodes |= {currentNode}
                currentNode = adder(currentNode,va)

            currentNode = adder(L[b],vb)
            while isInGrid(currentNode):
                part2Antinodes |= {currentNode}
                currentNode = adder(currentNode,vb)

part2 = len(part2Antinodes)
print(f"Part 1: {part1}, Part 2: {part2}.")
