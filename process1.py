import numpy as np
import time

# Multiply two large matrices
start_time = time.time()
matrix_size = 10000
matrix_a = np.random.rand(matrix_size, matrix_size)
matrix_b = np.random.rand(matrix_size, matrix_size)
result_matrix = np.dot(matrix_a, matrix_b)
end_time = time.time()
time_elapsed = end_time - start_time
print("Time elapsed:", time_elapsed, "seconds")
