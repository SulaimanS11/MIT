def greedy_cow_transport(cow, weight):
    collection = []
    current = []
    track = []
    count = 0
    wait = 0
    car = sorted(cow.items(), key=lambda x: x[1], reverse=True)

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

        if count == len(cow.keys()):
            break
    return collection


def brute_cow_transport(cow, weight):
    collection = []
    current = []
    track = []
    count = 0
    wait = 0
    car = sorted(cow.items(), key=lambda x: x[1], reverse=True)
    
    while True:

    return collection



