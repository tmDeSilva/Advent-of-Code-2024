#Day 1 part 1, part 2
print(sum([abs(a-b) for a,b in zip(sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[0]),sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]))]))
print(sum([a*sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]).count(a) for a,b in zip(sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[0]),sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]))]))

#Day 2 part 1, part 2
print(sum([1 if ((l := [int(i) for i in line.split()]) == sorted(l) or l == sorted(l)[::-1]) and (min(d:= [abs(l[i+1] - l[i]) for i in range(len(l)-1)]) >= 1 and max(d) <= 3) else 0 for line in open("text.txt","r")]))
print(sum([1 if f(L:= [int(i) for i in line.split()]) else 1 if (v:=sum([1 if f((g:=lambda l,j : [l[ind] for ind in range(len(l)) if ind != j])(L,i)) else 0 for i in range(len(L))])) >= 1 else 0 for line in open("text.txt","r") if (f := lambda l : (l == sorted(l) or l == sorted(l)[::-1]) and (min(d:= [abs(l[i+1] - l[i]) for i in range(len(l)-1)]) >= 1 and max(d) <= 3)) is not None]))

#Day 3 part 1, part 2
exec("import re") or print(sum([(l:=[int(i) for i in iTuple])[0]*l[1] for iTuple in re.findall(r'mul\(*(\d+),*(\d+)\)',"".join([line.strip()for line in open("text.txt","r")]))]))
exec("import re") or print(sum([(l:=[int(i) for i in re.findall(r"mul\(*(\d+),*(\d+)\)",iTuple.group())[0]])[0]*l[1] if re.findall(r"do\(\)|don't\(\)",('do()' + "".join([line.strip()for line in open("text.txt","r")]))[0:iTuple.start()])[-1] == "do()" else 0 for iTuple in re.finditer(r"mul\((\d+),(\d+)\)","do()" + "".join([line.strip()for line in open("text.txt","r")]))]))
      
Day 4 part 1, part 2
print(sum([sum([1 if "".join(grid[i][j:j+4]) in {"XMAS", "SAMX"} else 0 for j in range(len(grid[0]))]) for i in range(len(grid))]) + sum([sum([1 if "".join(rotatedgrid[i][j:j+4]) in {"XMAS", "SAMX"} else 0 for j in range(len(rotatedgrid))]) for i in range(len(rotatedgrid))]) + sum([sum([1 if "".join([grid[i+d][j+d] for d in range(4)]) in {"XMAS", "SAMX"} else 0 for j in range(len(grid[0])-3)]) for i in range(len(grid)-3)]) + sum([sum([1 if "".join([grid[i+d][j-d] for d in range(4)]) in {"XMAS", "SAMX"} else 0 for j in range(3,len(grid[0]))]) for i in range(len(grid)-3)])) if (grid := [tuple(line.strip()) for line in open("text.txt","r")], rotatedgrid := tuple(zip(*grid))) is not None else []
print(sum([sum([1 if "".join([grid[i+d][j+d] for d in range(3)]) in {"MAS", "SAM"} and "".join([grid[i+d][j+(2-d)] for d in range(3)]) in {"MAS", "SAM"}else 0 for j in range(len(grid[0]) - 2)]) for i in range(len(grid) - 2)])) if (grid := [tuple(line.strip()) for line in open("text.txt","r")]) is not None else []
