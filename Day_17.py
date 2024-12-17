import re

registersString, programString = open("text.txt","r").read().split("\n\n")
registers  = list(map(int, re.findall("(\d+)", registersString)))
flatProgram  = list(map(int, re.findall("(\d+)", programString)))
program = [(flatProgram[i], flatProgram[i+1]) for i in range(0,len(flatProgram),2)]

A,B,C = registers
reg = {"A": A, "B": B, "C": C}

part1 = ""
part2 = 0

def getCombo(x):
    if x <= 3:
        return x
    else:
        return reg["ABC"[x - 4]]
    
def _0(x,y):
    return reg["A"] // 2 ** getCombo(y), "A"

def _1(x,y):
    return reg["B"]^y, "B"

def _2(x,y):
    return getCombo(y) % 8, "B"

def _3(x,y):
    return y, "J"

def _4(x,y):
    return reg["B"] ^ reg["C"] , "B"

def _5(x,y):
    return getCombo(y) % 8, "O"

def _6(x,y):
    return _0(x,y)[0], "B"

def _7(x,y):
    return _0(x,y)[0], "C"

functions = [_0, _1, _2, _3, _4, _5, _6, _7]


PC = 0
output = []
while PC < len(program):
    opcode, operand = program[PC]
    res, action = functions[opcode](opcode, operand)

    if action in "ABC":
        reg[action] = res
    elif action == "J":
        if reg["A"] != 0:
            PC = res
            PC -= 1
    else:
        output.append(res)

    PC += 1

part1 = ",".join(map(str,output))

def getOutputbyA(pA):
    reg["A"] = pA
    reg["B"] = 0
    reg["C"] = 0
    for iPC in range(len(program)-2): #ignore out(5), jnz(3)
        opcode, operand = program[iPC]
        res, action = functions[opcode](opcode, operand)
        reg[action] = res
    return reg["B"] % 8

def getFullOutput(pA):
    res = [getOutputbyA(pA)]
    if pA//2**3 == 0:
        return res
    res += getFullOutput(pA//2**3)
    return res

def getPossibleA(pA = 0, i = 0):
    possible = set()
    if i == len(flatProgram):
        return {pA}
    for n in range(8*pA, 8*(pA+1)):
        if getOutputbyA(n) == flatProgram[-(i+1)]:
            for iN in getPossibleA(n,i+1):
                possible |= {iN}

    return possible

part2 = min(getPossibleA())
print(f"Part 1: {part1}, Part 2: {part2}.")
