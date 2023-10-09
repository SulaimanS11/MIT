# The harmonic sum of an integer n > 0 can be calculated using this formula 1 + 1/2 + .. + 1/n
import numbers
from ssl import HAS_TLSv1
import time
import copy


def factorials(num):  # recursion for finding factorials
    if num == 1:
        return 1
    else:
        time.sleep(1)
        print(num)
        return num * factorials(num - 1)

# 1/1 + 1/2 + 1/3 ... 1/n


def harmonicSums(num):
    """Returns the harmonic sum of the inputted number"""
    if num == 0:
        return 0
    else:
        return harmonicSums(num-1) + 1/num
# 1/1 + 1/2 + 1/3 + 1/4 = 2.083333333333333



print(harmonicSums(4))
