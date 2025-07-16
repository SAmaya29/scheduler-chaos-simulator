from abc import ABC, abstractmethod

class SchedulingAlgorithm(ABC):
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def add_process(self, process):
        pass

    @abstractmethod
    def get_next_process(self, current_time):
        pass

    @abstractmethod
    def on_tick(self, current_time):
        pass