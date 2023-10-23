import psutil

def get_cpu_temperature():
    temp = psutil.sensors_battery()
    return temp

print("CPU Temperature: ", get_cpu_temperature())