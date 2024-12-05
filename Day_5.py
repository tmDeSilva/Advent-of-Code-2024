rules, sets = "".join(open("text.txt","r").read()).split("\n\n")
rules = set([tuple([int(i) for i in rule.strip().split("|")]) for rule in rules.split("\n")])
sets = [[int(i) for i in lilset.strip().split(",")] for lilset in sets.split("\n")]
part1 = 0
part2 = 0

for iSet in sets:
    ordered = True

    for rule in rules:
        if rule[0] in iSet and rule[1] in iSet:
            if iSet.index(rule[0]) > iSet.index(rule[1]):
                ordered = False

    if ordered:
        part1 += iSet[(len(iSet))//2]
 
def specialSort(pSet):
    if len(pSet) <= 1:
        return list(pSet)

    above = []
    below = []
    base = pSet[0]

    for e in pSet:
        if base != e:
            if (base,e) in rules:
                above.append(e)
            else:
                below.append(e)

    return specialSort(tuple(below)) + [base] + specialSort(tuple(above))

for iSet in sets:
    l = specialSort(iSet)
    if l != iSet:
        part2 += l[len(l)//2]

print(f"Part 1: {part1}, Part 2: {part2}.")
