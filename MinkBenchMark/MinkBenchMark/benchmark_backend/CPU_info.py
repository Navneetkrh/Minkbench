import psutil
import time
import platform
import subprocess

# Cores Data

def physical_core_count():
    p_c_c = psutil.cpu_count(logical=False)
    return p_c_c

def logical_core_count():
    l_c_c = psutil.cpu_count(logical=True)
    return l_c_c

# Battery data

def Battery_info():
    Battery_percent = psutil.sensors_battery()
    return round(Battery_percent.percent,2)


# Frequency data

def current_freq():
    freq_current = psutil.cpu_freq().current / 1000
    return freq_current

def max_freq():
    freq_max = psutil.cpu_freq().max / 1000
    return freq_max

# RAM info

def memory_usage():
    mem = psutil.virtual_memory().percent
    return mem

def Max_ram():
    ram_info = psutil.virtual_memory()
    ram = f"{ram_info.total / (1024 ** 3):.2f}"
    return ram

def available_ram():
    avail = psutil.virtual_memory().available / (1024**3)
    return avail

def used_ram():
    used_ram = psutil.virtual_memory().used / (1024**3)
    return used_ram


# System info

def network_name():
    network = platform.node()
    return network

def machine_name():
    machine = platform.machine()
    return machine

def cpu_name():
    cpu_info = subprocess.check_output("wmic cpu get name", shell=True)
    cpu_model = cpu_info.decode("utf-8").strip().split("\n")[-1]
    return cpu_model

def platform_name():
    plat_name = platform.platform()
    return plat_name

def OS_name():
    os = platform.system()
    return os

def OS_release():
    os_r = platform.release()
    return os_r

def OS_version():
    os_v = platform.version()
    return os_v


# Secondary Memory info

def secondary_mem_space():
    sm = psutil.disk_usage().total
    sm = round(sm / (1024**3),2)
    return sm

def num_disks():
    num_d = len(psutil.disk_partitions())
    return num_d


# CPU Interrupt

def cntxt_switches():
    cnt = psutil.cpu_stats().ctx_switches
    return cnt

def interrupts_count():
    intt = psutil.cpu_stats().interrupts
    return intt

def sys_calls():
    sys_call = psutil.cpu_stats().syscalls
    return sys_call



# DISK operations

def read_count():
    temp = psutil.disk_io_counters().read_count
    return temp

def write_count():
    temp = psutil.disk_io_counters().write_count
    return temp

def read_bytes():
    temp = psutil.disk_io_counters().read_bytes
    return temp

def write_bytes():
    temp = psutil.disk_io_counters().write_bytes
    return temp

def used_space():
    temp = psutil.disk_usage().used/(1024**3)
    return temp

def free_space():
    temp = psutil.disk_usage().free/(1024**3)
    return temp

def disk_percent_usage():
    temp = psutil.disk_usage().percent
    return temp


# Network info

def Num_of_network():
    temp = len(psutil.net_connections())
    return temp

# Processes info

def process_data():
    import pandas as pd
    temp_ = psutil.test()
    temp_ = pd.DataFrame(temp)
    return temp_


# Cache info

def get_l2_capacity():
    import subprocess
    result = subprocess.check_output("wmic cpu get L2CacheSize, L3CacheSize", shell=True)
    cache_info = result.decode('utf-8').strip().split('\n')[1:] 
    cache_info = [line.strip().split() for line in cache_info]
    return line[0]

def get_l3_capacity():
    import subprocess
    result = subprocess.check_output("wmic cpu get L2CacheSize, L3CacheSize", shell=True)
    cache_info = result.decode('utf-8').strip().split('\n')[1:] 
    cache_info = [line.strip().split() for line in cache_info]
    return line[1]
