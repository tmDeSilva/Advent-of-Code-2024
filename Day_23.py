import re
nodesDict = {}

for line in open("text.txt","r"):
    node1,node2 = re.search("(\w+)-(\w+)",line).groups()

    if node1 in nodesDict.keys():
        nodesDict[node1].add(node2)
    else:
        nodesDict[node1] = {node2}
    
    if node2 in nodesDict.keys():
        nodesDict[node2].add(node1)
    else:
        nodesDict[node2] = {node1}

trios = set()

for nodeA in nodesDict.keys():
    if nodeA[0] == "t":
        for nodeB in nodesDict[nodeA]:
            for nodeC in nodesDict[nodeA]:
                if nodeB != nodeC:
                    if nodeB in nodesDict[nodeC]:
                        trios.add(tuple(sorted((nodeA,nodeB,nodeC))))

part1 = len(trios)

def findParty(startNode, visited):
    if startNode in visited:
        return visited
    visited |= {startNode}
    for nextNode in nodesDict[startNode]:
        invited = True
        for node in visited:
            if nextNode not in nodesDict[node]:
                invited = False
                break
        if invited:
            visited |= findParty(nextNode, visited | {nextNode})
    
    return visited

passwords = []
nodesList = list(nodesDict.keys())

while len(nodesList) > 0:
    starter = nodesList.pop(0)
    party = findParty(starter,set())
    passwords.append((len(party),",".join(sorted(list(party)))))

part2 = sorted(passwords)[-1][1]

print(f"Part 1: {part1}, Part 2: {part2}.")
