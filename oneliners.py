#Day 1 part 1, part 2
print(sum([abs(a-b) for a,b in zip(sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[0]),sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]))]))
print(sum([a*sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]).count(a) for a,b in zip(sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[0]),sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]))]))

#Day 2 part 1, part 2
print(sum([1 if ((l := [int(i) for i in line.split()]) == sorted(l) or l == sorted(l)[::-1]) and (min(d:= [abs(l[i+1] - l[i]) for i in range(len(l)-1)]) >= 1 and max(d) <= 3) else 0 for line in open("text.txt","r")]))
print(sum([1 if f(L:= [int(i) for i in line.split()]) else 1 if (v:=sum([1 if f((g:=lambda l,j : [l[ind] for ind in range(len(l)) if ind != j])(L,i)) else 0 for i in range(len(L))])) >= 1 else 0 for line in open("text.txt","r") if (f := lambda l : (l == sorted(l) or l == sorted(l)[::-1]) and (min(d:= [abs(l[i+1] - l[i]) for i in range(len(l)-1)]) >= 1 and max(d) <= 3)) is not None]))

#Day 3 part 1, part 2
exec("import re") or print(sum([(l:=[int(i) for i in iTuple])[0]*l[1] for iTuple in re.findall(r'mul\(*(\d+),*(\d+)\)',"".join([line.strip()for line in open("text.txt","r")]))]))
exec("import re") or print(sum([(l:=[int(i) for i in re.findall(r"mul\(*(\d+),*(\d+)\)",iTuple.group())[0]])[0]*l[1] if re.findall(r"do\(\)|don't\(\)",('do()' + "".join([line.strip()for line in open("text.txt","r")]))[0:iTuple.start()])[-1] == "do()" else 0 for iTuple in re.finditer(r"mul\((\d+),(\d+)\)","do()" + "".join([line.strip()for line in open("text.txt","r")]))]))
      
#Day 4 part 1, part 2
print(sum([sum([1 if "".join(grid[i][j:j+4]) in {"XMAS", "SAMX"} else 0 for j in range(len(grid[0]))]) for i in range(len(grid))]) + sum([sum([1 if "".join(rotatedgrid[i][j:j+4]) in {"XMAS", "SAMX"} else 0 for j in range(len(rotatedgrid))]) for i in range(len(rotatedgrid))]) + sum([sum([1 if "".join([grid[i+d][j+d] for d in range(4)]) in {"XMAS", "SAMX"} else 0 for j in range(len(grid[0])-3)]) for i in range(len(grid)-3)]) + sum([sum([1 if "".join([grid[i+d][j-d] for d in range(4)]) in {"XMAS", "SAMX"} else 0 for j in range(3,len(grid[0]))]) for i in range(len(grid)-3)])) if (grid := [tuple(line.strip()) for line in open("text.txt","r")], rotatedgrid := tuple(zip(*grid))) is not None else []
print(sum([sum([1 if "".join([grid[i+d][j+d] for d in range(3)]) in {"MAS", "SAM"} and "".join([grid[i+d][j+(2-d)] for d in range(3)]) in {"MAS", "SAM"}else 0 for j in range(len(grid[0]) - 2)]) for i in range(len(grid) - 2)])) if (grid := [tuple(line.strip()) for line in open("text.txt","r")]) is not None else []

#Day 5 part 1, part 2
print(sum([iSet[len(iSet)//2] if [1 if iSet.index(a) < iSet.index(b) else 0 for a,b in [list(map(int,s.split("|"))) for s in data[0].split("\n")]if a in iSet and b in iSet].count(0) == 0 else 0 for iSet in [list(map(int,s.split(","))) for s in data[1].split("\n")]])) if (data:= "".join(open("text.txt","r").read()).split("\n\n")) is not None else ()
print(sum([(f:=lambda pSet : pSet if len(pSet) <= 1 else f([e for e in pSet if e != (base := pSet[0]) and [e,base] in (pOrders := tuple([list(map(int,s.split("|"))) for s in data[0].split("\n")]))]) + [base] + f([e for e in pSet if e != base and [base,e] in pOrders]))(iSet)[len(iSet)//2] if [1 if iSet.index(a) < iSet.index(b) else 0 for a,b in set([tuple(map(int,s.split("|"))) for s in data[0].split("\n")]) if a in iSet and b in iSet].count(0) > 0 else 0 for iSet in tuple([tuple(map(int,s.split(","))) for s in data[1].split("\n")])])) if (data:= tuple("".join(open("text.txt","r").read()).split("\n\n"))) is not None else ()

#Day 6 part 1
exec("import sys") or exec ("sys.setrecursionlimit(10000)") or print(len((f:= lambda pos = (iX,iY), dir = 0, visited = set():  visited if not(0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid)) else f(pos, (dir + 1) % 4, visited | {pos}) if grid[(y:=pos[1] + dirs[dir][1])][(x:=pos[0] + dirs[dir][0])] == "#" else f((x,y), dir, visited | {pos}))())) if (grid := [list(line.strip()) for line in open("text.txt","r").readlines()]) and (dirs := [(0,-1),(1,0),(0,1),(-1,0)]) and (iY := (val := "".join(open("text.txt","r").read().split("\n")).find("^")) // len(grid[0])) and (iX := val % len(grid[0])) is not None else ()

#Day 7 part 1, part 2
(re:=__import__('re')), print(sum([target if [(f := lambda pNumbers, instructions, counter = 0, res = 0: res if counter == len(pNumbers)  else f(pNumbers,instructions, counter + 1, addMul[instructions[counter]](res,pNumbers[counter])))(numbers, getBin(i, len(numbers))) for i in range(2**(len(numbers) - 1))].count(target) > 0 else 0 for row in numberArray if (target := row[0]) and (numbers := row[1:])])) if (numberArray := [list(map(int,re.findall("(\d+)",line))) for line in open("text.txt","r").readlines()]) and (addMul := [lambda x,y: x+y, lambda x,y: x*y]) and (getBin := lambda x, power, binList = []: binList if power == 0 else getBin(x%(2**(power-1)), power - 1, binList + [x//(2**(power-1))])) is not None else None
(re:=__import__('re')), print(sum([target if [(f := lambda pNumbers, instructions, counter = 0, res = 0: res if counter == len(pNumbers)  else f(pNumbers,instructions, counter + 1, operations[instructions[counter]](res,pNumbers[counter])))(numbers, getBin(i, len(numbers))) for i in range(base**(len(numbers) - 1))].count(target) > 0 else 0 for row in numberArray if (target := row[0]) and (numbers := row[1:])])) if (numberArray := [list(map(int,re.findall("(\d+)",line))) for line in open("text.txt","r").readlines()]) and (getLen := lambda x, power = 1: power if 10 ** power > x else getLen(x,power + 1)) and (operations := [lambda x,y: x+y, lambda x,y: x*y, lambda x,y: x * 10 ** getLen(y) + y]) and (base := len(operations)) and (getBin := lambda x, power, binList = []: binList if power == 0 else getBin(x%(base**(power-1)), power - 1, binList + [x//(base**(power-1))])) is not None else None

#Day 8 part 1
print(sum([1 if check(iPoint) else 0 for iPoint in points])) if (points := set().union(*[set().union(*[set().union(*[set([tuple(va := (A:= np.array((L:=freqs[freq])[a])) + (delta := (A - (B:=np.array(L[b]))))), tuple(vb := B + (B - A))]) for b in range(a+1, len(freqs[freq]))]) for a in range(len(freqs[freq]) - 1)]) for freq in freqs.keys()]) if (grid := [list(line.strip()) for line in open("text.txt","r").readlines()]) and (np := __import__('numpy')) and (antennaPoints := [(grid[(y := n//len(grid[0]))][(x:= n%len(grid[0]))],(x,y)) for n in range(len(grid[0]) * len(grid)) if grid[n//len(grid[0])][n%len(grid[0])] != "."]) and (defaultdict:= __import__('collections').defaultdict) and (freqs := dict((f:=lambda pList, mergedDict = defaultdict(list): mergedDict if len(pList) == 0 else f(pList[1:],(mergedDict[pList[0][0]].append(pList[0][1]),mergedDict)[1]))(antennaPoints))) and (check := lambda point:  0 <= point[0] < len(grid[0]) and 0 <= point[1] < len(grid)) is not None else None) is not None else None

#Day 9 part 1
__import__('sys').setrecursionlimit(100000), print(sum([fragments[i] * i  if fragments[i] != -1 else 0 for i in range(len(fragments))])) if (line := list(map(int,open("text.txt","r").read().strip()))) and (fragments := (f := lambda array, freeC, fileC: array if fileC <= freeC else f(array, freeC, fileC - 1) if array[fileC] == -1 else array.__setitem__(freeC, array[fileC]) or array.__setitem__(fileC, -1) or f(array, freeC + 1, fileC) if array[freeC] == -1 else f(array, freeC + 1, fileC))((files:=[i//2 if i % 2 == 0 else -1 for i in range(len(line)) for _ in range(int(line[i]))]), 0, len(files) - 1)) is not None else []

#Day 10 part 1, part 2
print(sum([len((f := lambda start, trailends = set(): {start} if (val := grid[start[1]][start[0]]) == 9 else trailends | set.union(*newEnds) if (newEnds := [f(next, trailends) for iDir in dirs if grid[(next := addV(start, iDir))[1]][next[0]] == val + 1]) else set())(trailhead)) for trailhead in trailheads])) if (grid := [list(map(int,line.strip())) for line in open("text.txt").readlines()]) and (trailheads := [(j,i) for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j] == 0]) and (dirs := [(1,0),(0,1),(-1,0),(0,-1)]) and (addV := lambda v1, v2: res if inGrid(res := (v1[0]+v2[0], v1[1]+v2[1])) else v1) and (inGrid := lambda p: 0 <= p[0] < len(grid[0]) and 0 <= p[1] < len(grid)) is not None else None
print(sum([(f := lambda start, paths = 0: 1 if (val := grid[start[1]][start[0]]) == 9 else paths + sum([f(next, paths) for iDir in dirs if grid[(next := addV(start, iDir))[1]][next[0]] == val + 1]))(trailhead) for trailhead in trailheads])) if (grid := [list(map(int,line.strip())) for line in open("text.txt").readlines()]) and (trailheads := [(j,i) for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j] == 0]) and (dirs := [(1,0),(0,1),(-1,0),(0,-1)]) and (addV := lambda v1, v2: res if inGrid(res := (v1[0]+v2[0], v1[1]+v2[1])) else v1) and (inGrid := lambda p: 0 <= p[0] < len(grid[0]) and 0 <= p[1] < len(grid)) is not None else None

#Day 11 part 1
print(sum([f(number, 25) for number in numbers])) if (numbers := list(map(int, open("text.txt").read().strip().split()))) and (getLen := lambda x, power = 1: power if 10 ** power > x else getLen(x,power+1)) and (f := lambda rock, blinks: 1 if blinks == 0 else f(1,blinks - 1) if rock == 0 else f(rock * 2024, blinks - 1) if (length := getLen(rock)) % 2 == 1 else f(rock // (10 ** (length//2)),blinks - 1) + f(rock % (10 ** (length//2)), blinks - 1)) is not None else None
