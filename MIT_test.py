# boollist = [True, True]

# if sum(boollist) == len(boollist):
#     print("I love Titties")
# else:
#     print("NO")

# honda = {"h": 1, "i": 1, 'c': 1, 'z': 1, 'm': 2, 'a': 1}


# def rec(n):
#     score = 0
#     print(score, "0")
#     score += 1
#     n += "cat"
#     print(score, "1")
#     if score > 10:
#         return None
#     return rec(n) + score


# print(rec("rat"))

# class Weird(object):
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x

#     def getX(self):
#         return #x

#     def getY(self):
#         return #y


# class Wild(object):
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x

#     def getX(self):
#         return self.x

#     def getY(self):
#         return self.y


# X = 7
# Y = 8

# # w1 = Weird(X, Y)
# # print(w1.getX())

# w2 = Wild(X, Y)
# w3 = Wild(17, 18)
# w4 = Wild(X, 18)

# X = w4.getX() + w3.getX() + w2.getX()
# print(X)
# print(w4.getX())
# Y = w4.getY() + w3.getY()
# Y = Y + w2.getY()
# print(Y)
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        if self.getX() == other.getX() and self.getY() == other.getY():
            return True
        else:
            return False

    def __repr__(self):
        return "Coordinate({},{})".format(self.x, self.y)


# c1 = Coordinate(3, 5)
# c2 = Coordinate(3, 8)
# print(eval(repr(c1)) == c2)


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        sim = []
        for y in self.vals:
            for n in other.vals:
                if y == n:
                    sim.append(str(y))

        if len(sim) == 0:
            return "{}"
        else:
            sim.sort()
            return "{" + ",".join(sim) + "}"

    def __len__(self):
        return len(self.vals)


# bob = intSet()
# bob.insert(3)
# bob.insert(4)
# bob.insert(5)
# bob.insert(6)

# bob2 = intSet()
# bob2.insert(434242)
# bob2.insert(3)
# bob2.insert(4)
# bob2.insert(31)

# print(bob.intersect(bob2))
# print(len(bob))

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'


def studySpell(spell):
    print(spell)


# spell = Accio()
# spell.execute()
# studySpell(spell)
# studySpell(Confundo())

word = "jgnnq"
letters = 'abcdefghijklmnopqrstuvwxyz'
lettersLower = [k for k in letters]
lettersUpper = [j.upper() for j in letters]
lettersLower.sort(reverse=True)
lettersUpper.sort(reverse=True)

carl = ''
while True:
    # mark = word.split()
    for n in range(26):
        for y in word:
            y = lettersLower[lettersLower.index(y)-n]
            carl += y
        if carl == "hello":
            break
        else:
            carl = ''
            continue
