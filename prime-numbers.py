import itertools
import math
import pandas as pd
from sympy import isprime
import numpy as np

my_list = [2, 3, 5, 7, 11] # Prime numbers to use



all_combinations = []

# Loop from length 1 up to the length of the list
for r in range(1, len(my_list) + 2):
    combinations_object = itertools.combinations_with_replacement(my_list, r)
    all_combinations.extend(combinations_object)

df = pd.DataFrame({"Inputs":all_combinations})

df['Product'] = df["Inputs"].map(lambda x: math.prod(x))
df['Product+1_is_prime'] = df["Product"].map(lambda z: isprime(z+1))






print(df.to_string(index=False))
print("---------- Rows that do not follow the hypothesis ------------------")

print(df[(df['Product'] % 2 != 0) & df['Product+1_is_prime']])

# If the product is even, then the product+1 is always prime
