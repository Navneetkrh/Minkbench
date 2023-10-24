import sympy
import time

# create the start time
start_time = time.time()
n = 100000000  # Calculate primes up to a certain number
primes = list(sympy.primerange(1, n))
print(primes)
# create the end time
end_time = time.time()
# calculate the difference between the two times
time_elapsed = end_time - start_time
# print the time elapsed
print("Time elapsed:", time_elapsed, "seconds")
