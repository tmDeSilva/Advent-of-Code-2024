file = [line.strip() for line in open("text.txt","r")]

part1 = 0
part2 = 0

for line in file:
    safe = False
    sequence = [int(i) for i in line.split()]
    deltas = [abs(sequence[i+1] - sequence[i]) for i in range(len(sequence)-1)]

    if (sorted(sequence) == sequence or sorted(sequence) == sequence[::-1]) and (min(deltas) >= 1 and max(deltas) <= 3):
        part1 += 1
        safe = True
        

    if not safe:
        for i in range(len(sequence)):
            deleted = sequence.pop(i)

            deltas = [abs(sequence[i+1] - sequence[i]) for i in range(len(sequence)-1)]
            if (sorted(sequence) == sequence or sorted(sequence) == sequence[::-1]) and (min(deltas) >= 1 and max(deltas) <= 3):
                safe = True
            
            sequence.insert(i,deleted)

    if safe:
        part2 += 1

print(f"Part 1: {part1}, Part 2: {part2}.")
