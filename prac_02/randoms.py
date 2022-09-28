"""CP1404 | Prac_02 Random Numbers | Dannielle Jones"""

import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Line 1: What was the smallest number you could have seen, what was the largest?
# A: Smallest: 5, Largest: 20

# Line 2: What was the smallest number you could have seen, what was the largest?
# A: Smallest: 3, Largest: 9
# Line 2: Could line 2 have produced a 4?
# A: No, it could not only 3, 5, 7 and 9

# Line 3: What was the smallest number you could have seen, what was the largest?
# A: Smallest: 2.5, Largest: 5.5

# Produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))

