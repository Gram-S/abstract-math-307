import itertools
import math

my_list = [2, 3, 5]
all_combinations = []

# Loop from length 1 up to the length of the list
for r in range(1, len(my_list) + 2):
    combinations_object = itertools.combinations_with_replacement(my_list, r)
    all_combinations.extend(combinations_object)

all_combinations.sort(key=math.prod)

for i in all_combinations:
    print(i, '->', math.prod(i))
