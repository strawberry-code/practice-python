import random

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)
result_overlaps = [i for i in set(a) if i in b]
result = [i for i in result_overlaps if result_overlaps.count(i) == 1]
print(a)
print(b)
print(result)
