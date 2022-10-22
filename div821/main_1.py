numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    firstLine = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]

    arrayLen = firstLine[0]
    k = firstLine[1]
    tempK = k

    msum = 0
    for i in range(k):
        maxi = 0
        for j in range(i, arrayLen, k):
            if array[j] > maxi:
                maxi = array[j]
        msum += maxi
    print(msum)


