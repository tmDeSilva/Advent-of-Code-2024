file = [int(line.strip()) for line in open("text.txt","r").readlines()]

part1 = 0
part2 = 0
pricesArr = []
deltasArr = []
deltaScores = {}

for secretNumber in file:
    prices = []
    for _ in range(2000):
        secretNumber  = ((secretNumber * 64)^secretNumber)%16777216
        secretNumber = ((secretNumber//32)^secretNumber)%16777216
        secretNumber = ((secretNumber*2048)^secretNumber)%16777216
        prices.append(secretNumber%10)

    part1 += secretNumber
    pricesArr.append(prices)
    deltasArr.append([prices[i+1]-prices[i] for i in range(len(prices)-1)])


for j in range(len(pricesArr)):
    seen = set()
    for i in range(len(pricesArr[0])-4):
        key = tuple(deltasArr[j][i:i+4])
        if key not in seen:
            seen |= {key}
            if key not in deltaScores.keys():
                deltaScores[key] = pricesArr[j][i+4]
            else:
                deltaScores[key] += pricesArr[j][i+4]

part2 = max(deltaScores.values())
print(f"Part 1: {part1}, Part 2: {part2}.")
