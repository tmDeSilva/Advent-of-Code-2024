#Day 1 part 1, part 2
print(sum([abs(a-b) for a,b in zip(sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[0]),sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]))]))
print(sum([a*sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]).count(a) for a,b in zip(sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[0]),sorted(list(zip(*[[int(i) for i in line.strip().split()] for line in open("text.txt","r")]))[1]))]))
