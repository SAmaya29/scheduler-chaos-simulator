import random

class InterruptionPerturbation:
    def apply(self, simulator_state):
        if simulator_state["running_process"]:
            simulator_state["running_process"].set_state("WAITING")
            simulator_state["waiting_queue"].append(simulator_state["running_process"])
            simulator_state["logger"].info(f"[Chaos] System interruption: PID {simulator_state['running_process'].pid} sent to waiting queue")
            simulator_state["running_process"] = None