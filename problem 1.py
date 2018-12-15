multiples = []
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        multiples += [i]
sum = 0
for i in multiples:
    sum += i
print(sum)

# Output: 233168