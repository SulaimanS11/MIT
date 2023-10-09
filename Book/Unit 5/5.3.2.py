# Write a list comprehension that generates all non-primes betweem from 2 to 100

nonp = list({x for x in range(2, 100) for y in range(2, x) if x % y == 0})
print(nonp)
