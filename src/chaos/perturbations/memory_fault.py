import random

class MemoryFaultPerturbation:
    def apply(self, simulator_state):
        if simulator_state["ready_queue"]:
            p = random.choice(simulator_state["ready_queue"])
            extra = random.randint(10, 100)
            p.memory_required += extra
            simulator_state["logger"].info(f"[Chaos] Memory fault injected in PID {p.pid}: +{extra} MB")