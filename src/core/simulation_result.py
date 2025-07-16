import json
import csv

class SimulationResult:
    def __init__(self, metrics_report, completed_processes, metrics):
        self.metrics_report = metrics_report
        self.completed_processes = completed_processes
        self.metrics = metrics

    def generate_report(self, output_file=None):
        lines = []
        lines.append("==== Simulation Report ====")
        for k, v in self.metrics_report.items():
            lines.append(f"{k}: {v}")
        if output_file:
            with open(output_file, "w") as f:
                f.write("\n".join(lines))
        else:
            print("\n".join(lines))

    def plot_metrics(self):
        from src.visualization.plots import plot_gantt, plot_metrics
        plot_gantt(self.completed_processes)
        plot_metrics(self.metrics)

    def export_csv(self, file_path):
        with open(file_path, mode="w", newline="") as csvfile:
            fieldnames = [
                "pid", "priority", "burst_time", "arrival_time", "memory_required",
                "state", "wait_time", "turnaround_time", "response_time", "finish_time", "process_type"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for p in self.completed_processes:
                writer.writerow({
                    "pid": p.pid,
                    "priority": p.priority,
                    "burst_time": p.burst_time,
                    "arrival_time": p.arrival_time,
                    "memory_required": p.memory_required,
                    "state": p.state,
                    "wait_time": getattr(p, "wait_time", None),
                    "turnaround_time": getattr(p, "turnaround_time", None),
                    "response_time": getattr(p, "response_time", None),
                    "finish_time": getattr(p, "finish_time", None),
                    "process_type": getattr(p, "process_type", None),
                })

    def export_json(self, file_path):
        data = {
            "metrics": self.metrics_report,
            "processes": [
                {
                    "pid": p.pid,
                    "priority": p.priority,
                    "burst_time": p.burst_time,
                    "arrival_time": p.arrival_time,
                    "memory_required": p.memory_required,
                    "state": str(p.state),
                    "wait_time": getattr(p, "wait_time", None),
                    "turnaround_time": getattr(p, "turnaround_time", None),
                    "response_time": getattr(p, "response_time", None),
                    "finish_time": getattr(p, "finish_time", None),
                    "process_type": getattr(p, "process_type", None),
                }
                for p in self.completed_processes
            ]
        }
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)

    def plot_heatmap(self):
        from src.visualization.plots import plot_heatmap_resource_usage
        total_time = self.metrics.total_time
        plot_heatmap_resource_usage(self.completed_processes, total_time)