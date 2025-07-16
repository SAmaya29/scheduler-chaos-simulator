import random

class LatencyPerturbation:
    def __init__(self, max_delay=5):
        self.max_delay = max_delay

    def apply(self, simulator_state):
        delay = random.randint(1, self.max_delay)
        simulator_state["current_time"] += delay
        simulator_state["logger"].info(f"[Chaos] Latency injected: {delay} ticks")