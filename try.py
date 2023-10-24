import psutil

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

def temp(data):
    sensor1 = data['nvme']
    sensor2 = data['nvme']
    avg_temp = (sensor1[1][1] + sensor2[1][1])/2
    print(avg_temp)

data = psutil.sensors_temperatures()
temp(data)