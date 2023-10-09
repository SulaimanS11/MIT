class Location:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self, deltax, deltay):
        return Location(self.x + deltax, self.y + deltay)
    
    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x-ox
        yDist = self.y-oy

        return (xDist**2 + yDist**2)**0.5
        
    def __str__(self):
        return f"<{str(self.x)}, {str(self.y)}>"

class Field:
    def __init__(self):
        self.drunks = {}

    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError("Dupe Drunk")
        else:
            self.drunks[drunk] = loc

    def getLoc(self,drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not on field")
        return self.drunks[drunk]

    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunks not on field")
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

from matplotlib import pyplot as pylab
import random

class Drunk:
    def __init__(self, name= None):
        self.name = name
    def __str__(self):
        if self.name != None:
            return self.name
        return "Anonymous"

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,0.9),(0.0,-1.1),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)
    
def walk(f,d,numsteps):
    """Assumes f a field, d a Drunk in f, & numsteps an int => 0"""
    start = f.getLoc(d)
    for s in range(numsteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numsteps, numTrials, dClass):
    Homer = dClass()
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f,Homer,numsteps),1))
    return distances



#DRUNK TEST

def drunkTest(walkLengths, numTrials, dClass):
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials,dClass)
        print(dClass.__name__, "Random Walk of", numSteps, "steps")
        print(" Mean =", round(sum(distances)/len(distances),4))
        print(" Max =", max(distances), "min =", min(distances))
    
def SimAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)


# drunkTest((0,1,2),100,UsualDrunk)
# SimAll((UsualDrunk, ColdDrunk), (1,10,100,1000), 100)
class styleIterator:
    def __init__(self,styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) -1:
            self.index = 0
        else:
            self.index +=1 
        return result

def simDrunk(numTrials,dClass,walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print("Starting Simlulations of", numSteps, "steps")
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)

    return meanDistances

def simAll(drunkKinds,walkLengths,numTrials):
    styleChoice = styleIterator(("m-","b--","g--"))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print("starting simulation of", dClass.__name__)
        means = simDrunk(numTrials,dClass,walkLengths)
        pylab.plot(walkLengths,means,curStyle,label=dClass.__name__)
    pylab.title(f"mean dist from org {numTrials} trials")
    pylab.xlabel("numb of steps")
    pylab.ylabel("dist from org")
    pylab.legend(loc = "best")

numSteps = (10,100,1000,10000)
# simAll((UsualDrunk, ColdDrunk), numSteps, 100)
# pylab.show()