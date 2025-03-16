import re
import numpy as np
import matplotlib.pyplot as plt

# Read timing results
with open("timing_results.txt", "r") as file:
    lines = file.readlines()

# Extract execution times
n_procs = []
times_fully_parallel = []
times_chunked_parallel = []
times_serial = None

current_n_proc = None
collect_fully_parallel = False
collect_chunked_parallel = False

for i, line in enumerate(lines):
    print(f"Processing line {i}: {line.strip()}")  # Debugging print

    # Match the line indicating the number of processes
    match = re.search(r"Running with (\d+) processes", line)
    if match:
        current_n_proc = int(match.group(1))
        n_procs.append(current_n_proc)
        collect_chunked_parallel = True  # First script: chunked parallel
        print(f"Found n_proc: {current_n_proc}")

    # Match chunked parallel execution time
    if collect_chunked_parallel:
        match_chunked = re.search(r"real\s+(\d+)m([\d.]+)s", line)
        if match_chunked:
            time_chunked = int(match_chunked.group(1)) * 60 + float(match_chunked.group(2))
            times_chunked_parallel.append(time_chunked)
            collect_chunked_parallel = False
            collect_fully_parallel = True  # Second script: fully parallel
            continue
            print(f"Found chunked parallel time: {time_chunked}s")

    # Match fully parallel execution time
    if collect_fully_parallel:
        match_fully_parallel = re.search(r"real\s+(\d+)m([\d.]+)s", line)
        if match_fully_parallel:
            time_fully = int(match_fully_parallel.group(1)) * 60 + float(match_fully_parallel.group(2))
            times_fully_parallel.append(time_fully)
            collect_fully_parallel = False  # Reset flag
            print(f"Found fully parallel time: {time_fully}s")

    # Match the serial execution time
    if "Running serial implementation" in line:
        print("Detected serial implementation run.")
        for j in range(i + 1, len(lines)):  # Look ahead in lines to find the real time
            match_serial = re.search(r"real\s+(\d+)m([\d.]+)s", lines[j])
            if match_serial:
                times_serial = int(match_serial.group(1)) * 60 + float(match_serial.group(2))
                print(f"Found serial time: {times_serial}s")
                break

# Debugging prints to check extracted data
print(f"Final n_procs: {n_procs}")
print(f"Final times_chunked_parallel: {times_chunked_parallel}")
print(f"Final times_fully_parallel: {times_fully_parallel}")
print(f"Serial execution time: {times_serial}")

# Ensure valid data
if times_serial is None:
    raise ValueError("Serial time not found in the input file.")
if len(times_fully_parallel) != len(n_procs) or len(times_chunked_parallel) != len(n_procs):
    raise ValueError("Mismatch between number of processes and recorded times.")

# Convert lists to numpy arrays
n_procs = np.array(n_procs)
times_fully_parallel = np.array(times_fully_parallel)
times_chunked_parallel = np.array(times_chunked_parallel)
times_serial = np.full_like(n_procs, times_serial)  # Serial time is constant

# Plot execution times
fig, ax = plt.subplots(1,3, figsize=(15,5))

ax[0].plot(n_procs, times_chunked_parallel, marker="o", linestyle="-", label="Chunked Parallel")
ax[1].plot(n_procs, times_fully_parallel, marker="s", linestyle="--", label="Fully Parallel")
ax[2].plot(n_procs, times_serial, marker="^", linestyle=":", label="Serial Execution")

for i in range(3):
    ax[i].set_xlabel("Number of Processes")
    ax[i].set_ylabel("Execution Time (seconds)")
    ax[i].set_title("Execution Time vs. Number of Processes")
    ax[i].legend()
    ax[i].grid()
    
plt.savefig('parallel.png')
plt.show()
