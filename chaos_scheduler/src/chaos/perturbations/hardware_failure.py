class HardwareFailurePerturbation:
    def __init__(self, freeze_time=3):
        self.freeze_time = freeze_time

    def apply(self, simulator_state):
        simulator_state["logger"].info(f"[Chaos] Hardware failure: Scheduler frozen for {self.freeze_time} ticks")
        simulator_state["current_time"] += self.freeze_time