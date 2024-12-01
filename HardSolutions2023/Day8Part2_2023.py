instructions, nodeData = "".join(open("text.txt","r").readlines()).split("\n\n")

instructions = [0 if instructions[i] == "L" else 1 for i in range(len(instructions.strip()))]

nodeData = [line.strip().split(" = ") for line in nodeData.split("\n")]
dicto = {}
for line in nodeData:
    dicto[line[0]] = line[1][1:-1].split(", ")

startKeys = []
for key in dicto.keys():
    if key[-1] == "A":
        startKeys.append(key)


stepsList = []
for startKey in startKeys:
    node = startKey
    I = 0
    l = []
    
    while node[-1] != "Z" or len(l) == 0:
        l.append(node)
        node = dicto[node][instructions[I]]
        I += 1
        I %= len(instructions)

    stepsList.append(len(l))


def lcm(x,y):
    def hcf(a,b):
        while b:
            a,b = b, a%b
        return a
    return (x*y)//hcf(x,y)

res = 1
for step in stepsList:
    res = lcm(res, step)

print(res)
