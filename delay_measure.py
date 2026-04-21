import subprocess
import re

def measure_delay(host):
    print(f"\nPinging {host}...\n")

    result = subprocess.run(["ping", "-c", "5", host], capture_output=True, text=True)
    output = result.stdout

    print(output)

    match = re.search(r'rtt min/avg/max/mdev = (.*) ms', output)

    if match:
        rtt = match.group(1).split('/')
        print("\n--- RTT Analysis ---")
        print("Min RTT :", rtt[0], "ms")
        print("Avg RTT :", rtt[1], "ms")
        print("Max RTT :", rtt[2], "ms")
    else:
        print("RTT not found")

if __name__ == "__main__":
    target = input("Enter target IP: ")
    measure_delay(target)