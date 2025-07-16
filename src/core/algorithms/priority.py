from .base import SchedulingAlgorithm

class PriorityScheduling(SchedulingAlgorithm):
    def __init__(self, preemptive=False):
        self.ready_queue = []
        self.preemptive = preemptive
        self.current_process = None

    def add_process(self, process):
        self.ready_queue.append(process)
        self.ready_queue.sort(key=lambda p: p.priority)

    def get_next_process(self, current_time):
        if self.preemptive or not self.current_process:
            if self.ready_queue:
                self.current_process = self.ready_queue.pop(0)
            else:
                self.current_process = None
        return self.current_process

    def on_tick(self, current_time):
        if self.preemptive:
            self.ready_queue.sort(key=lambda p: p.priority)