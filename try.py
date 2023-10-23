import subprocess


def get_number_of_disks():
    output = (
        subprocess.check_output(["lsblk", "-d", "-n", "--output=NAME"])
        .decode("utf-8")
        .strip()
    )
    disk_list = output.split("\n")
    return len(disk_list)


if __name__ == "__main__":
    num_disks = get_number_of_disks()
    print(f"Number of Disks: {num_disks}")


import subprocess


def get_motherboard_info():
    try:
        output = subprocess.check_output(["dmidecode", "--type", "2"]).decode("utf-8")
        return output
    except subprocess.CalledProcessError as e:
        return "N/A"


if __name__ == "__main__":
    motherboard_info = get_motherboard_info()
    print(f"Motherboard Info:\n{motherboard_info}")
