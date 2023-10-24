import psutil
import subprocess

# Get the number of open file handles for the current process

# temprature
# num_handles = psutil.sensors_temperatures()
# print(f"Number of Open File Handles: {num_handles}")

#process
# num_handles = len(psutil.pids())

# print(f"Number of Open File Handles: {num_handles}")

# print no of disk partitions
# num_handles = len(psutil.disk_partitions())
# print(f"Number of Open File Handles: {num_handles}")

# print(psutil.disk_partitions())

# def temp(data):
#     sensor1 = data['nvme']
#     sensor2 = data['nvme']
#     avg_temp = (sensor1[1][1] + sensor2[1][1])/2
#     print(avg_temp)

# data = psutil.sensors_temperatures()
# temp(data)

# temp = psutil.sensors_fans()
# print(temp)

# def get_l2_capacity():
#     import subprocess
#     result = subprocess.check_output("wmic cpu get L2CacheSize, L3CacheSize", shell=True)
#     cache_info = result.decode('utf-8').strip().split('\n')[1:] 
#     cache_info = [line.strip().split() for line in cache_info]
#     return line[0]

# def get_l3_capacity():
#     import subprocess
#     result = subprocess.check_output("wmic cpu get L2CacheSize, L3CacheSize", shell=True)
#     cache_info = result.decode('utf-8').strip().split('\n')[1:] 
#     cache_info = [line.strip().split() for line in cache_info]
#     return line[1]

# print(get_l2_capacity())
# print(get_l3_capacity())

import subprocess

import subprocess

def get_l2_cache_size():
    try:
        # Run the 'lscpu | grep "L2 cache"' command and capture its output
        output = subprocess.check_output(['lscpu', '|', 'grep', '"L2 cache"'], universal_newlines=True, shell=True)

        # Extract the L2 cache size from the output
        l2_cache_size = output.strip().split()[-1]

        return l2_cache_size

    except subprocess.CalledProcessError:
        return None

if __name__ == "_main_":
    l2_cache_size = get_l2_cache_size()

    if l2_cache_size:
        print(f"L2 Cache Size: {l2_cache_size}")
    else:
        print("Error: Unable to retrieve L2 cache size.")
        
