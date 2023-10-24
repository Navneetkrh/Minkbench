import psutil
import platform
import subprocess
import datetime

# Backend Data Extraction
# CPU % Utilization
cpu_utilization = psutil.cpu_percent(interval=1)

# MM % Utilization (assuming you mean Memory or RAM)
ram_utilization = psutil.virtual_memory().percent

# CPU Temperature (may not be available on all Windows systems)
try:
    # This command assumes you have Open Hardware Monitor installed and running.
    output = subprocess.check_output("ohmcli.exe -s -f temperature", shell=True)
    cpu_temperature = output.decode("utf-8").strip()
except Exception as e:
    cpu_temperature = "N/A"

# Start time, Present time, Completion time stamps
start_time = datetime.datetime.now()
present_time = start_time  # You can update this later as needed
completion_time = None  # Set this when the process is complete

# Power consumption (if available and measurable)
power_consumption = None  # You would need external hardware or tools for this

# CPU Clock Monitor (GHz)
cpu_info = platform.processor()
cpu_clock = f"{psutil.cpu_freq().current / 1000:.2f} GHz"

# Cores (data)
cores = psutil.cpu_count(logical=False)  # Physical CPU cores

# General System Info
ram_info = psutil.virtual_memory()
ram = f"{ram_info.total / (1024 ** 3):.2f} GB"  # RAM in gigabytes

secondary_memory = f"{psutil.disk_usage('/').total / (1024 ** 3):.2f} GB"  # Secondary memory in gigabytes
num_disks = len(psutil.disk_partitions())
motherboard_info = "N/A"  # Requires specific tools or access to hardware info
ram_slots = "N/A"  # RAM slots may not be directly available via software on Windows

# This command may not work on all Windows systems; you can replace it with a command that works on your system.
try:
    cpu_info = subprocess.check_output("wmic cpu get name", shell=True)
    cpu_model = cpu_info.decode("utf-8").strip().split("\n")[-1]
except Exception as e:
    cpu_model = "N/A"

os_info = platform.uname()
os_name = os_info.system
os_version = os_info.release

# Print or use the extracted information as needed
print("Backend Data Extraction:")
print(f"CPU % Utilization: {cpu_utilization}%")
print(f"RAM % Utilization: {ram_utilization}%")
print(f"CPU Temperature: {cpu_temperature}")
print(f"Start Time: {start_time}")
print(f"Present Time: {present_time}")
print(f"Completion Time: {completion_time}")
print(f"Power Consumption: {power_consumption}")
print(f"CPU Clock Monitor: {cpu_clock}")
print(f"Cores (Data): {cores}")

print("\nGeneral System Info:")
print(f"RAM: {ram}")
print(f"Secondary Memory: {secondary_memory}")
print(f"Number of Disks: {num_disks}")
print(f"Motherboard No.: {motherboard_info}")
print(f"RAM Slots: {ram_slots}")
print(f"CPU Model: {cpu_model}")
print(f"OS: {os_name} {os_version}")


import psutil

def get_cpu_temperature():
    temp = psutil.sensors_battery()
    return temp

print("CPU Temperature: ", get_cpu_temperature())