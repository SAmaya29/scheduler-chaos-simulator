class Experiment:
    def __init__(self, workload, duration, chaos_config, processes):
        self.workload = workload
        self.duration = duration
        self.chaos_config = chaos_config
        self.processes = processes