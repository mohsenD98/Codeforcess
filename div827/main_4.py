def gcd(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)

numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    length = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()

    flag = False
    for i in range(length-1, 1, -1):
        if gcd(arr[i],arr[i-1]) == 1:
            print(arr[i], arr[i-1])
            flag = True
            break
    if not flag:
        print("-1")