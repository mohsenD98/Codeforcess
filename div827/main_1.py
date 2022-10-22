numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    arr = [int(x) for x in input().split()]  

    flag = False
    for a in arr:
        if a == sum(arr) - a:
            print("YES")
            flag = True
            break

    if not flag:
        print("NO")


