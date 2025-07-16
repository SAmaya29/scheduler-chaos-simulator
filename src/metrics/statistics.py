import numpy as np

class Statistics:
    def __init__(self):
        self.wait_times = []
        self.turnaround_times = []
        self.response_times = []
        self.cpu_utilization = []
        self.completed_processes = 0
        self.total_time = 0
        self.process_wait_times = []
        self.process_turnarounds = []

    def record_process(self, process):
        self.wait_times.append(process.wait_time)
        self.process_wait_times.append(process.wait_time)
        self.turnaround_times.append(process.turnaround_time)
        self.process_turnarounds.append(process.turnaround_time)
        if process.response_time is not None:
            self.response_times.append(process.response_time)
        self.completed_processes += 1

    def advanced_fairness_index(self):
        waits = np.array(self.process_wait_times)
        if len(waits) == 0:
            return 1.0
        numerator = np.sum(waits) ** 2
        denominator = len(waits) * np.sum(waits ** 2)
        if denominator == 0:
            return 1.0
        return numerator / denominator

    def starvation_count(self, threshold=0.8):
        starved = 0
        for w, t in zip(self.process_wait_times, self.process_turnarounds):
            if t > 0 and w / t > threshold:
                starved += 1
        return starved

    def report(self):
        return {
            "avg_wait_time": np.mean(self.wait_times) if self.wait_times else 0,
            "avg_turnaround": np.mean(self.turnaround_times) if self.turnaround_times else 0,
            "avg_response_time": np.mean(self.response_times) if self.response_times else 0,
            "throughput": self.completed_processes / self.total_time if self.total_time else 0,
            "cpu_utilization": np.mean(self.cpu_utilization) if self.cpu_utilization else 0,
            "fairness_index": self.advanced_fairness_index(),
            "starvation_count": self.starvation_count(),
        }