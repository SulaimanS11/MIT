###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,weight=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    collection = []
    current = []
    track = []
    count = 0
    wait = 0
    car = sorted(cows.items(), key=lambda x: x[1], reverse=True)

    while True:
        for k, v in car:
            if wait + v <= weight:
                if k not in track:
                    current.append(k)
                    track.append(k)
                    count += 1
                    wait += v

        collection.append(current)
        wait = 0
        current = []

        if count == len(cows.keys()):
            break
    return collection



# Problem 2
def brute_force_cow_transport(cow, weight=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows = [n for n in get_partitions(cow)]
    valid_cows = []
    total = 0
    red = 1
    # print(cows)


    for n in cows:
        for x in n:
            for y in x:
                total += cow[y]
            if len(n) == 1 and total <= weight:
                return n
            if total > weight:
                red = 1
            total = 0

        if red == 0:
            valid_cows.append(n)
        red = 0
    
    bob = valid_cows[0]
    for n in valid_cows:
        if len(n) < len(bob):
            bob = n
    
    return bob

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("P\MIT\MIT 6.002\pset1\ps1_cow_data.txt")
limit=10
# print(cows)

# print(greedy_cow_transport({"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}, limit))
# for n in get_partitions(cows):
#     print(n)
print(brute_force_cow_transport({'Buttercup': 11, 'Betsy': 39, 'Luna': 41, 'Starlight': 54}, 145))


