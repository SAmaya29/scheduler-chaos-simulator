from .base import SchedulingAlgorithm

class SJF(SchedulingAlgorithm):
    def __init__(self):
        self.ready_queue = []

    def add_process(self, process):
        self.ready_queue.append(process)
        self.ready_queue.sort(key=lambda p: p.burst_time)

    def get_next_process(self, current_time):
        if self.ready_queue:
            return self.ready_queue.pop(0)
        return None

    def on_tick(self, current_time):
        pass