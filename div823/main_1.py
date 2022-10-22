numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    inputs = [int(x) for x in input().split()]
    numberOfPlanets = inputs[0]
    costOfSecondMachineUsage = inputs[1]
    
    plantsOrbit = [int(x) for x in input().split()]
    orbits = set(plantsOrbit)

    if costOfSecondMachineUsage == 1:
        print(len(orbits))
        continue

    costSum = 0
    for planet in orbits:
        planetCount = plantsOrbit.count(planet)
        if costOfSecondMachineUsage < planetCount:
            costSum += costOfSecondMachineUsage
        else: 
            costSum += planetCount
    
    print(costSum)