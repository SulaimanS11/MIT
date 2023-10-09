balance = 320000
annualInterestRate = 0.2
months = 12
balance2 = balance

upperB = (balance + (balance*annualInterestRate)) / 12
lowerB = balance / 12
middleB = 0
lowestPay = 0

number = 0

while True:
    balance2 = balance
    middleB = ((upperB + lowerB) / 2)
    for per in range(months):
        balance2 -= middleB
        balance2 += (annualInterestRate / 12) * balance2

    number += 1

    if balance2 > 0:
        lowerB = middleB
    elif abs(balance2) <= 0.04:
        lowestPay = middleB
        break
    else:
        upperB = middleB

roundedP = round(lowestPay, 2)
print("Lowest Payment: {}".format(roundedP))
print(balance2)
print(number)
