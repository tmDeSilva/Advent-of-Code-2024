#Day 1 part 1, part 2
print(sum([abs(a-b) for a,b in zip(sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[0]),sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]))]))
print(sum([a*sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]).count(a) for a,b in zip(sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[0]),sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]))]))

#Day 2 part 1, part 2
print(sum([1 if ((l := [int(i) for i in line.split()]) == sorted(l) or l == sorted(l)[::-1]) and (min(d:= [abs(l[i+1] - l[i]) for i in range(len(l)-1)]) >= 1 and max(d) <= 3) else 0 for line in open("text.txt","r")]))
print(sum([1 if f(L:= [int(i) for i in line.split()]) else 1 if (v:=sum([1 if f((g:=lambda l,j : [l[ind] for ind in range(len(l)) if ind != j])(L,i)) else 0 for i in range(len(L))])) >= 1 else 0 for line in open("text.txt","r") if (f := lambda l : (l == sorted(l) or l == sorted(l)[::-1]) and (min(d:= [abs(l[i+1] - l[i]) for i in range(len(l)-1)]) >= 1 and max(d) <= 3)) is not None]))
