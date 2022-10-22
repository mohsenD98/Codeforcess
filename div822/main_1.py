numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    numberOfSticks = int(input())

    stickLenghts = [int(x) for x in input().split()]

    alreadyDone = False
    for stickLen in set(stickLenghts):
        if stickLenghts.count(stickLen) >= 3:
            print(0)
            alreadyDone = True
            break
        
    if alreadyDone: continue

    stickLenghts.sort()
    minOp = 100000000000000
    for index in range(-1, numberOfSticks-3):
        a = stickLenghts[index+1]
        b = stickLenghts[index+2]
        c = stickLenghts[index+3]
        result = ((b-a) + (c-b))
        if minOp > result: 
            minOp = result
    print(minOp)
