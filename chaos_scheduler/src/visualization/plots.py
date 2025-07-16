import matplotlib.pyplot as plt
import numpy as np

def plot_gantt(processes):
    plt.figure(figsize=(10, 2 + len(processes)//2))
    for i, p in enumerate(processes):
        plt.barh(y=p.pid, left=p.arrival_time, width=p.turnaround_time, height=0.5)
    plt.xlabel("Time")
    plt.ylabel("PID")
    plt.title("Gantt Chart of Process Execution")
    plt.show()

def plot_metrics(metrics):
    plt.figure()
    plt.plot(metrics.cpu_utilization, label="CPU Utilization")
    plt.xlabel("Time")
    plt.ylabel("Utilization")
    plt.legend()
    plt.title("CPU Utilization Over Time")
    plt.show()

def plot_heatmap_resource_usage(processes, total_time):
    n = len(processes)
    times = np.arange(total_time)
    usage = np.zeros((n, total_time))
    pid_to_idx = {p.pid: idx for idx, p in enumerate(processes)}

    for p in processes:
        start = p.arrival_time
        end = getattr(p, "finish_time", start + p.burst_time)
        usage[pid_to_idx[p.pid], start:end] = 1

    plt.figure(figsize=(12, 6))
    plt.imshow(usage, aspect="auto", cmap="hot", interpolation="nearest")
    plt.xlabel("Time")
    plt.ylabel("Process (PID)")
    plt.title("Heatmap of CPU Usage per Process")
    plt.colorbar(label="CPU Usage")
    plt.yticks(range(n), [p.pid for p in processes])
    plt.show()