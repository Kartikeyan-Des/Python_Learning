import time
import random
import numpy as np

salaries = [random.randint(20000, 200000) for _ in range(1_000_000)]

start = time.time()

result = []
for salary in salaries:
    bonus = salary * 0.10         
    after_bonus = salary + bonus   
    tax = after_bonus * 0.18     
    take_home = after_bonus - tax 
    result.append(take_home)

end = time.time()

# print(f"First 5 results: {result[:100]}")
# print(f"Loop took: {end - start:.4f} seconds")

salaries_np = np.array(salaries)

start_np = time.time()

after_bonus_np = salaries_np * 1.10

take_home_np = after_bonus_np *0.82

end_np = time.time()

print(f"First 5 results: {take_home_np[:5]}")
print(f"NumPy took: {end_np - start_np:.4f} seconds")
print(f"NumPy is {(end - start) / (end_np - start_np):.1f}x faster")
