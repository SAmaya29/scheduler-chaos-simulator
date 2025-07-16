from .base import SchedulingAlgorithm

class MultilevelQueue(SchedulingAlgorithm):
    def __init__(self, levels=3):
        self.levels = levels
        self.queues = [[] for _ in range(levels)]

    def add_process(self, process):
        level = min(process.priority, self.levels - 1)
        self.queues[level].append(process)

    def get_next_process(self, current_time):
        for queue in self.queues:
            if queue:
                return queue.pop(0)
        return None

    def on_tick(self, current_time):
        pass