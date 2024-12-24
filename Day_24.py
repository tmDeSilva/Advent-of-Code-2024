#Constants
gates = ["AND", "XOR", "OR"]
gateFunctions = {"AND":lambda x,y: (x and y), "OR": lambda x,y: (x or y), "XOR": lambda x,y: x^y}
ERROR = "xxx"

#Parse Input
initialString, gateString  = open("text.txt","r").read().split("\n\n")
initialWires = [line.strip().split(": ") for line in initialString.split("\n")]
gateConnections = [line.strip() for line in gateString.split("\n")]

#Part 1 Global Variables
part1 = 0
wires = {}
completeOperations = 0
gateData = []
outputted = set()
zBitLength = 0

#Part 2 Global variables
part2 = ""
gateOutDict = {}
carryWires = []
swapped = []

for wire, bit in initialWires:
    wires[wire] = int(bit)

for line in gateConnections:
    operation, outWire = line.split(" -> ")
    gateOutDict[operation] = outWire

    for gate in gates:
        if gate in operation:
            wire1, wire2 = operation.split(f" {gate} ")
            gateOutDict[f"{wire2} {gate} {wire1}"] = outWire
            gateData.append((gate, wire1, wire2, outWire))
            break

while completeOperations < len(gateConnections):
    for gate, wire1, wire2, outWire in gateData:
        if wire1 in wires.keys() and wire2 in wires.keys():
            if outWire in outputted:
                continue

            outBit = gateFunctions[gate](wires[wire1], wires[wire2])
            wires[outWire] = outBit
 
            completeOperations += 1
            outputted.add(outWire)

            if outWire[0] == "z":
                part1 += 2 ** (bit := int(outWire[1:])) * outBit
                if bit > zBitLength:
                    zBitLength = bit

#Part 2 functions
def createKey(pWireType, pBit):
    return pWireType + "0" * (2- len(str(pBit))) + str(pBit)

def getVal(pOperation):
    return gateOutDict[pOperation] if pOperation in gateOutDict.keys() else ERROR

def OpAddLSB(pXKey,pYKey):
    pOutDict = {}
    op1 = f"{pXKey} XOR {pYKey}"
    op2 = f"{pXKey} AND {pYKey}"
    pA = getVal(op1)
    pB = getVal(op2)

    pOutDict[pA] = op1
    pOutDict[pB] = op2

    return pA, pB, pOutDict

def OpBitwiseAdd(pXKey,pYKey, pCarry):
    pA, pB, pOutDict = OpAddLSB(pXKey,pYKey)
    opOut = f"{pCarry} XOR {pA}"
    pOut = getVal(opOut)
    opC1 = f"{pCarry} AND {pA}"
    pC = getVal(f"{pCarry} AND {pA}")
    opNC = f"{pB} OR {pC}"
    pNewCarry = getVal(opNC)

    pOutDict[pOut] = opOut
    pOutDict[pC] = opC1
    pOutDict[pNewCarry] = opNC
    
    return pA, pB, pOut, pC, pNewCarry, pOutDict

def swap(wire1, wire2, pDict, pValToKey):
    pDict[pValToKey[wire1]] = wire2
    pDict[pValToKey[wire2]] = wire1

    return pDict

for bit in range(zBitLength - 1):
    xKey = createKey("x",bit)
    yKey = createKey("y",bit)

    if bit == 0:
        A, B, wireToOp = OpAddLSB(xKey, yKey)
        carryWires.append(B)

    if bit >= 1:
        carry = carryWires[-1]
        A,B, outWire, C, newCarry, wireToOp = OpBitwiseAdd(xKey, yKey, carry)

        zMisplaced = False
        realOutWire = ""
        for wire in [A,B,C, carry, newCarry]:
            if wire[0] == "z":
                realOutWire = wire
                zMisplaced = True
                break

        if zMisplaced:
            swapped += (iSwapped := [outWire,realOutWire])
            gateOutDict = swap(*iSwapped, gateOutDict, wireToOp)
        
        elif outWire == ERROR:
            swapped += (iSwapped := [A,B])
            gateOutDict = swap(*iSwapped, gateOutDict, wireToOp)

        A,B, outWire, C, newCarry, wireToOp = OpBitwiseAdd(xKey, yKey, carry)
        carryWires.append(newCarry)

part2 = ",".join(sorted(set(swapped)))
print(f"Part 1: {part1}, Part 2: {part2}.")
