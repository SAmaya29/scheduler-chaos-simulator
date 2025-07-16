import random

class CPUOverloadPerturbation:
    def apply(self, simulator_state):
        if simulator_state["running_process"]:
            overload = random.randint(2, 10)
            simulator_state["running_process"].burst_time += overload
            simulator_state["logger"].info(f"[Chaos] CPU overload: Burst time of PID {simulator_state['running_process'].pid} increased by {overload}")