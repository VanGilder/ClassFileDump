# Generate a dataset of N = 100,000 numbers (between 1 and 100)

import random

N = 100000
data = [random.randint(1, 100) for _ in range(N)]

# Generate Q = 10 queries (between 1 and 100)
Q = 10
queries = [random.randint(1, 100) for _ in range(Q)]

# Write these numbers into a file named "input.dat"
with open("input.dat", "w") as f:
    f.write(str(N) + "\n")
    f.write(" ".join(map(str, data)) + "\n")
    f.write(str(Q) + "\n")
    f.write(" ".join(map(str, queries)))

