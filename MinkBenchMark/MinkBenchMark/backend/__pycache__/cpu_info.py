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