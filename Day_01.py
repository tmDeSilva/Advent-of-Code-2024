# Global Variables #
Part1 = 0
Part2 = 0

rhs, lhs = []
grid = [[]]

# Main code #
grid = [[int(i) for i in line.strip().split()] for line in open("text.txt","r")]

#The zip function effectively rotates the grid
#Note: rhs is short for right hand side and lhs for left hand side
rhs, lhs = zip(*grid)
rhs = sorted(rhs)
lhs = sorted(lhs)

#Part 1 loop
for rhsNumber,lhsNumber in zip(rhs,lhs):
    #Find the absolute
    Part1 += abs(rhsNumber - lhsNumber)

#Part 2 loop
for rhsNumber in rhs:
    #Find the number of times the rhs number appears in the lhs
    Part2 += rhsNumber * lhs.count(rhsNumber)

# Result #
print(f"Part 1: {Part1}, Part 2: {Part2}.")
