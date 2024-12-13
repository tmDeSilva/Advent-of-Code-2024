import re
data = [list(map(int, tuple(re.findall("(\d+)",line)))) for line in open("text.txt","r").read().split("\n\n")]

part1 = 0
part2 = 0

def buttonPresses(pAdx,pAdy,pBdx,pBdy,pPrizeX,pPrizeY):
    pAPresses =  (pPrizeX*pBdy - pBdx*pPrizeY)/(pAdx*pBdy - pAdy*pBdx)
    pBPresses = (pPrizeX*pAdy - pAdx*pPrizeY)/(pBdx*pAdy - pAdx*pBdy)

    return 3* pAPresses + pBPresses if pAPresses % 1 ==0 and pBPresses % 1 == 0 else 0
 
error = 1e13
for Adx,Ady,Bdx,Bdy,prizeX,prizeY in data:
    part1 += buttonPresses(Adx,Ady,Bdx,Bdy,prizeX,prizeY)
    part2 += buttonPresses(Adx,Ady,Bdx,Bdy,prizeX + error,prizeY + error)

print(f"Part 1: {int(part1)}, Part 2: {int(part2)}.")
