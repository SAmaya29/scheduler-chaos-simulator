from .base import SchedulingAlgorithm

class FCFS(SchedulingAlgorithm):
    def __init__(self):
        self.ready_queue = []

    def add_process(self, process):
        self.ready_queue.append(process)

    def get_next_process(self, current_time):
        if self.ready_queue:
            return self.ready_queue.pop(0)
        return None

    def on_tick(self, current_time):
        pass