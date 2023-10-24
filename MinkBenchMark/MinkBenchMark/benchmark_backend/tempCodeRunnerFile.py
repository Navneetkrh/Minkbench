import subprocess

def get_cache_info():
    try:
        result = subprocess.check_output("wmic cpu get L2CacheSize, L3CacheSize", shell=True)
        cache_info = result.decode('utf-8').strip().split('\n')[1:]  # Remove header and split lines
        cache_info = [line.strip().split() for line in cache_info]

        for line in cache_info:
            if len(line) == 2:
                print(f"Level 2 Cache Size: {line[0]}")
                print(f"Level 3 Cache Size: {line[1]}")
    
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve cache information.")

if __name__ == "__main__":
    get_cache_info()
