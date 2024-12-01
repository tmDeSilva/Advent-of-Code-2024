file = "".join(open("text2.txt","r").readlines()).split("\n\n")
seeds = [int(i) for i in file[0].split(": ")[1].split()]
vals =  []

from functools import lru_cache


@lru_cache(maxsize = None)
def splitRanges(plines, pRange):
    

    start,end = pRange
    res = []
    cond = True

    for i in range(len(plines)):
        b,_,c = plines[i]
        
        if start < b:
            if b <= end and end < b + c:
                cond = False
                res.append([start,b-1])
                res.append([b,end])
                break
        elif b + c <= end:
            if b <= start and start < b + c:
                cond = False
                res.append([start,b+c-1])
                res += splitRanges(plines[i+1:],tuple([b+c,end]))
                break
        elif b <= start and end < b + c:
            cond = False
            res.append([start,end])
            break
        elif start < b and b + c <= end:
            cond = False
            res.append([start,b-1])
            res.append([b,b+c-1])
            res += splitRanges(plines[i+1:],tuple([b+c,end]))
            break
    if cond:
        res.append([start,end])
    return res

for j in range(0,len(seeds),2):

    ranges = [[seeds[j], seeds[j] + seeds[j+1] - 1]]

    for i in range(1, len(file)):
        ranges = sorted(ranges)
        lines = tuple([tuple(int(e) for e in j.split()) for j in file[i].split(":\n")[1].split("\n")])
        newlines = []
        for a,b,c in lines:
            newlines.append((b,a,c))

        newlines = sorted(newlines)

        newRanges = []
        for iRange in ranges:
            RES =  splitRanges(tuple(newlines),tuple(iRange))

            for E in RES:
                if E not in newRanges:
                    newRanges.append(E)
   
        for j in range(len(newRanges)):
            A,B = newRanges[j]
            for b,a,c in newlines:
                if b <= A and B < b+c:
                    delta = a - b
                    newRanges[j] = [A + delta,B + delta]

        ranges = newRanges

    vals.append(min([d for d,_ in ranges]))

print(min(vals))
