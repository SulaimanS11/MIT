"""You have a bucket with 3 red balls and 3 green balls. Assume that once you draw a ball out of the 
   bucket, you don't replace it. What is the probability of drawing 3 balls of the same color?

Write a Monte Carlo simulation to solve the above problem. Feel free to write a helper function if you wish."""


# import random


# balls = ['r','r','r','g','g','g']
# print(random.choice(balls))


def monteBallosim(numTrials):
    import random
    w = 0

    for n in range(numTrials):
        balls = ['r','r','r','g','g','g']
        marcus = []
        for y in range(3):
            bob = random.choice(balls)
            rob = balls.pop(balls.index(bob))
            marcus.append(rob)
        
        if marcus.count("r") == 3 or marcus.count("g") == 3:
            w += 1
    
    return w/numTrials

# print(monteBallosim(100000))

