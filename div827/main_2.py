numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    length = int(input())
    arr = [int(x) for x in input().split()]  

    if len(set(arr)) == len(arr):
        print("YES")
    else:
        print("NO")

    

