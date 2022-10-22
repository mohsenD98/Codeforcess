numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    inputs = [int(x) for x in input().split()]
    n = inputs[0]
    k = inputs[1]
    r = inputs[2]
    c = inputs[3]

    for i in range(1,n+1):
        for j in range(1, n+1):
            if (i + j) % k == (r + c) % k:
                print("X", end="")
            else:
                print(".", end="")
        print("")