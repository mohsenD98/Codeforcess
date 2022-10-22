numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    rows = []
    for i in range(8):
        rows.append((input()))

    flag = False
    for row in rows:
        if list(row).count("R") < 8 and list(row).count("R") >= 1:
            print("B")
            flag = True
            break
    if flag: continue
    for i in range(8):
        mCol = []
        for row in rows:
            mCol.append(list(row)[i])

        if mCol.count("B") < 8 and mCol.count("B")>=1:
            print("R")
            flag = True
            break
    if flag: continue
    mFlag = False
    for row in rows:
        if row.count("R") > 1:
            print("R")
            mFlag = True
            break
    if not mFlag:
        print("B")

