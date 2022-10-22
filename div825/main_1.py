numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    length = int(input())
    arrA = [int(x) for x in input().split()]  
    arrB = [int(x) for x in input().split()]  
    if arrA == arrB:
        print(0)
        continue

    count1inA= arrA.count(1)
    count1inB= arrB.count(1)

    if count1inA == count1inB:
        print(1)
        continue

    temp = []
    for i in range(length):
        temp.append(arrB[i] - arrA[i])

    b1 = False
    b2 = False
    if temp.count(-1) > 0 : b1 = True
    if temp.count(1) > 0 : b2 = True
    
    if b1 and b2 :
        print(1 + abs(count1inA - count1inB))
    
    else:
        print(abs(count1inA - count1inB))