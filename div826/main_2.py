import math

numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    n = int(input())

    if n == 3 :
        print(-1)
        continue

    if n % 2 == 0 : 
        for i in range(n, 0, -1):
            print(i, end = "")
            print(" ", end="")

    elif n % 2 == 1 : 
        for i in range(n, math.ceil(n/2), -1):
            print(i, end = "")  
            print(" ", end="")
        for i in range(1, math.ceil(n/2)+1, 1):
            print(i, end = "")  
            print(" ", end="")