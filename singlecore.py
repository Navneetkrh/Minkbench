import os
import multiprocessing
import time


def single_core_task():
    # Limit the process to run on a single core (core 0).
    os.sched_setaffinity(0, {0})

    for _ in range(1, 100000000):
        _ = 1  # Perform a CPU-bound operation

    # print single core score
    print("Single core score:", multiprocessing.cpu_count())


if __name__ == "__main__":
    single_core_task()
