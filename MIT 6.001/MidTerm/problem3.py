def closest_power(base, num):
    power = 2  # the starting power
    number = base  # our increment var

    if int(num) == 0 or int(num) == 1:  # test if case
        return 0

    while number <= num:
        number = number ** base
        power += 1

    num1 = number - num

    num2 = (number/num) - num

    if abs(num1) < abs(num2):
        print("num1")
        return power

    elif abs(num2) < abs(num1):
        print("num2")
        return power-1


print(closest_power(4, 50))

# def closest_power(base, num):
#     '''
#     base: base of the exponential, integer > 1
#     num: number you want to be closest to, integer > 0
#     Find the integer exponent such that base**exponent is closest to num.
#     Note that the base**exponent may be either greater or smaller than num.
#     In case of a tie, return the smaller value.
#     Returns the exponent.
#     '''
#     num = int(num)
#     based = 0
#     temp = 0
#     for power in range(num):
#         based = base ** power
#         if based < num:
#             temp = power
#         if based >= num:
#             if (base ** power) - num >= abs((base ** temp) - num):
#                 return temp
#             else:
#                 return power


# print(closest_power(5, 375.0))
