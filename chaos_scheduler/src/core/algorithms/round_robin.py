from .base import SchedulingAlgorithm

class RoundRobin(SchedulingAlgorithm):
    def __init__(self, quantum=4):
        self.ready_queue = []
        self.quantum = quantum
        self.current_quantum = 0
        self.current_process = None

    def add_process(self, process):
        self.ready_queue.append(process)

    def get_next_process(self, current_time):
        if not self.current_process or self.current_quantum == 0:
            if self.current_process:
                self.ready_queue.append(self.current_process)
            if self.ready_queue:
                self.current_process = self.ready_queue.pop(0)
                self.current_quantum = self.quantum
            else:
                self.current_process = None
        return self.current_process

    def on_tick(self, current_time):
        if self.current_process:
            self.current_quantum -= 1
            if self.current_quantum == 0:
                if self.current_process.remaining_time > 0:
                    self.ready_queue.append(self.current_process)
                self.current_process = None