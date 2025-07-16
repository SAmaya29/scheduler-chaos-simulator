from enum import Enum, auto

class ProcessState(Enum):
    NEW = auto()
    READY = auto()
    RUNNING = auto()
    WAITING = auto()
    TERMINATED = auto()

class Process:
    def __init__(self, pid, priority, burst_time, arrival_time, memory_required, process_type="CPU-bound"):
        self.pid = pid
        self.priority = priority
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.memory_required = memory_required
        self.process_type = process_type

        self.state = ProcessState.NEW
        self.wait_time = 0
        self.turnaround_time = 0
        self.response_time = None
        self.remaining_time = burst_time
        self.finish_time = None
        self.history = []

    def set_state(self, new_state):
        self.history.append((self.state, new_state))
        self.state = new_state

    def update_stats(self, current_time):
        if self.state == ProcessState.TERMINATED:
            self.turnaround_time = self.finish_time - self.arrival_time

    def __repr__(self):
        return f"<Process pid={self.pid} state={self.state}>"