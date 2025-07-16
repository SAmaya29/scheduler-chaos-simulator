import random
from src.core.process import Process

def generate_workload(workload_type, num_processes, duration):
    processes = []
    for pid in range(num_processes):
        if workload_type == "high_cpu_bound":
            burst = random.randint(20, 50)
            mem = random.randint(50, 200)
            arrival = random.randint(0, duration//4)
            ptype = "CPU-bound"
        elif workload_type == "io_bound":
            burst = random.randint(5, 15)
            mem = random.randint(30, 100)
            arrival = random.randint(0, duration//2)
            ptype = "I/O-bound"
        else:  # mixed
            burst = random.randint(5, 40)
            mem = random.randint(30, 200)
            arrival = random.randint(0, duration//2)
            ptype = "mixed"
        priority = random.randint(0, 2)
        p = Process(pid, priority, burst, arrival, mem, process_type=ptype)
        processes.append(p)
    return processes