import multiprocessing
import time


def multi_core_task(iterations, core):
    for _ in range(iterations):
        _ = 1  # Perform a CPU-bound operation
    print(f"Process running on core {core}")


if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()

    processes = []
    iterations_per_core = 10000000

    for core in range(num_cores):
        process = multiprocessing.Process(
            target=multi_core_task, args=(iterations_per_core, core)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # print multi core score
    print("Multi core score:", multiprocessing.cpu_count())
