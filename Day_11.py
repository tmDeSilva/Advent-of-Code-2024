import time
stones = list(map(int,open("text.txt","r").read().strip().split()))

def getLength(pStone):
    res = 0
    while pStone // (10 ** res) != 0:
        res += 1
    return res

from functools import lru_cache
@lru_cache (maxsize = 1024)
def getStones(pStone, pTarget, pCount = 0):
    count = 0
    if pCount == pTarget:
        return 1
    else:
        if pStone == 0:
            count += getStones(1, pTarget, pCount + 1)
        elif (iLength := getLength(pStone))%2 == 0:
            count += getStones(pStone // (10**(iLength//2)), pTarget, pCount + 1)
            count += getStones(pStone % (10**(iLength//2)), pTarget, pCount + 1)
        else:
            count += getStones(2024*pStone, pTarget, pCount + 1)
    return count

initial = time.time()
part1 = 0
part2 = 0
for stone in stones:
    part1 += getStones(stone, 25)
    part2 += getStones(stone, 75)

timeTaken = time.time() - initial
print(f"Part 1: {part1}, Part 2: {part2} in {timeTaken:.2f}s.")
