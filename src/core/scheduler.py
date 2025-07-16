from src.core.algorithms import fcfs, sjf, round_robin, priority, multilevel_queue

ALGORITHMS = {
    "fcfs": fcfs.FCFS,
    "sjf": sjf.SJF,
    "round_robin": round_robin.RoundRobin,
    "priority": priority.PriorityScheduling,
    "multilevel_queue": multilevel_queue.MultilevelQueue,
}

class ChaosScheduler:
    def __init__(self, algorithm="fcfs", **kwargs):
        if algorithm not in ALGORITHMS:
            raise ValueError(f"Algoritmo '{algorithm}' no soportado.")
        self.algorithm = ALGORITHMS[algorithm](**kwargs)
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, event, data):
        for observer in self.observers:
            observer.update(event, data)

    def add_process(self, process):
        self.algorithm.add_process(process)

    def get_next_process(self, current_time):
        return self.algorithm.get_next_process(current_time)

    def on_tick(self, current_time):
        self.algorithm.on_tick(current_time)