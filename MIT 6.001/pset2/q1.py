import numbers


balance = 3329
annualInterestRate = 0.2
monthlyMinimum = 10
months = 12
balance2 = 0
number = 0
while True:
    balance2 = balance
    for per in range(months):
        balance2 -= monthlyMinimum
        balance2 += (annualInterestRate/12) * balance2
    number += 1
    if balance2 < 0:
        break
    else:
        monthlyMinimum += 10


print("Lowest Payment: {}".format(monthlyMinimum))
print(balance2)
print(number)
