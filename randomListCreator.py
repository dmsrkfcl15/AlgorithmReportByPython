import random

def makeRandomList(count):
    randomList = []
    if(count > 100):
        return False
    
    while(len(randomList) < count):
        randomNum = random.randrange(1, 101)
        if(not (randomNum in randomList)):
            randomList.append(randomNum)
            
    return randomList[:]

makeRandomList(20)