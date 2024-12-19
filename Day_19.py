import re
import time

initial = time.time()

towelsString, linesString = open("text.txt","r").read().split("\n\n")
towels = list(re.findall(r"\b\w+\b",towelsString.strip()))
lines = linesString.strip().split("\n")

from functools import lru_cache

@lru_cache (maxsize = None)
def getCombos(pLine):
    combos = 0
 
    if len(pLine) == 0:
        return 1
    
    for towel in towels:
        if len(towel) <= len(pLine):
            match = True
            for i in range(len(towel)):
                if towel[i] != pLine[i]:
                    match = False
                    break

            if match:
                combos += getCombos(pLine[len(towel):])

    return combos

part1 = 0
part2 = 0
for line in lines:
    val = getCombos(line)

    if val > 0:
        part1 += 1
        part2 += val

print(f"Part 1: {part1}, Part 2: {part2} in {time.time() - initial:.2f}s")
