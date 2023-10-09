def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    pass


# init values
dict = {1: 10, 2: 20, 3: 30, 4: 30}
keys = []
values = []
mult = []

# splitting keys and vals
for k, v in dict.items():
    keys.append(k)
    values.append(v)

print(keys, values)

for n in values:
    if values.count(n) > 1:
        mult.append(n)

newd = {}
# new dict comp
while len(newd.values()) < len(dict.values()):
    for n in range(len(keys)):
        newd[values[n]] = keys[n]


# print(newd)


def dict_invert(d):
    result = {}
    for x in d:
        if d[x] not in result:
            result[d[x]] = [x]
        else:
            result[d[x]].append(x)
            result[d[x]].sort()

    return result


d = {4: True, 2: True, 0: True}
print(dict_invert(d))
