numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    a, b = map(str,input().split())

    aLast = a[-1]
    bLast = b[-1]

    if aLast == "L" and bLast == "S":
        print(">")
    if aLast == "L" and bLast == "M":
        print(">")
    if aLast == "L" and bLast == "L":
        if len(a) == len(b):
            print("=")
        else:
            if len(a) < len(b):
                print("<")  
            else:
                print(">") 

    if aLast == "M" and bLast == "S":
        print(">")
    if aLast == "M" and bLast == "M":
        if len(a) == len(b):
            print("=")
        else:
            if len(a) < len(b):
                print(">")  
            else:
                print("<") 
    if aLast == "M" and bLast == "L":
        print("<")                                    

    if aLast == "S" and bLast == "S":
        if len(a) == len(b):
            print("=")
        else:
            if len(a) < len(b):
                print(">")  
            else:
                print("<") 
    if aLast == "S" and bLast == "M":
        print("<")
    if aLast == "S" and bLast == "L":
        print("<")                                    