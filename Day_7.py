import time
file = [line.strip().split(": ") for line in open("text.txt","r").readlines()]

def pad(pObject,pFinalLength, toPadWith):
    return (pFinalLength - len(pObject)) * toPadWith + pObject

def convertToBaseN(pNumber,base):
    res = []
    while pNumber != 0:
        res.append(pNumber % base)
        pNumber = pNumber // base
    return res[::-1]

part1 = 0
part2 = 0

initial = time.time()
for line in file:
    target, numbers = line
    target = int(target)
    numbers = [(int(n)) for n in numbers.split()]

    part1Found = False
    part2Found = False

    for i in range(2**(len(numbers)-1)):
        s = pad(convertToBaseN(i,2), len(numbers) -1, [0])
        R = numbers[0]
        for j in range(1,len(numbers)):

            if s[j-1] == 0:
                R = R + numbers[j]
            elif s[j-1] == 1:
                R = R * numbers[j]
            
        if R == target:
            part1Found = True

    if part1Found:
        part1 += target
        part2 += target
    else:
        for i in range(3**(len(numbers)-1)):
            l = pad(convertToBaseN(i,3),len(numbers)-1,[0])
            R = numbers[0]
            for j in range(1,len(numbers)):
                
                if l[j-1] == 0:
                    R = R + numbers[j]
                elif l[j-1] == 1:
                    R = R * numbers[j]
                elif l[j-1] == 2:
                    R = int(str(R) + str(numbers[j]))

            if R == target:
                part2Found = True

        if part2Found:
            part2 += target

print(f"Part 1 {part1}, Part 2 {part2}. Time taken: {time.time() - initial :.3f}s")
