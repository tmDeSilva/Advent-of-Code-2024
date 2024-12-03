from functools import lru_cache

def pad(pString,both = True):
    return f".{pString}." if both else f".{pString}"

#Use Lru_cache to remember the results of previous inputs, hence reducing execution time
@lru_cache(maxsize=None)
def getNumberOfCombos(pCode, pElements):

    count = 0
    springToMatch = ""

    #If all the elements have been placed and there are no disregarded broken springs, return 1 else 0
    if len(pElements) == 0:
        if "#" not in pCode:
            return 1
        else:
            return 0
    
    #If there are still elements but the springs have been used up return 0
    elif len(pCode) == 0:
        return 0
    
    springToMatch = pad(pElements[0] * "#")

    #If there is only one element remaining and it is a possibility for the remaining springs return 1 else 0
    if len(pElements) == 1:
        if len(springToMatch) == len(pCode):
            match = True
            for j in range(len(springToMatch)):
            
                if pCode[j] != "?":
                    if springToMatch[j] != pCode[j]:
                        match = False
            if match:
                return 1
            else:
                return 0
    
    #Try and see where the spring of length pElements[0] can go on the code
    for i in range(min(pCode.find("#") if "#" in pCode else len(pCode),len(pCode) - len(springToMatch)+1)):

        match = True
        
        for j in range(i, i + len(springToMatch)):
          
            if pCode[j] != "?":
                if springToMatch[j - i] != pCode[j]:
                    match = False

        if match:
            #RECURSION:
            #Disregard the first element and the part of the code where it has been placed and try to position the next spring
            count += getNumberOfCombos(pad(pCode[i+len(springToMatch):],False), pElements[1:])

    #Return the total number of arrangemenets found
    return count

part1 = 0
part2 = 0
FACTOR = 5
file = [line.strip().split() for line in open("text.txt","r")]

for i in range(len(file)):
    line = file[i]
    code, elements = line
    elements = [int(i) for i in elements.split(",")]
    elements = tuple(elements)

    part1Arrangements = getNumberOfCombos(pad(code),elements)
    part1 += part1Arrangements

    #Alter the code and elements tuple for part 2
    code = "?".join([code] * FACTOR)
    elements *= FACTOR
    part2Arrangements = getNumberOfCombos(pad(code),elements)
    part2 += part2Arrangements

print(f"Part 1: {part1}, Part 2: {part2}.")
