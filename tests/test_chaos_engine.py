from src.chaos.chaos_engine import ChaosEngine
from src.chaos.perturbations.latency import LatencyPerturbation

def test_latency_perturbation():
    state = {"current_time": 0, "ready_queue": [], "waiting_queue": [], "running_process": None, "logger": None}
    chaos = ChaosEngine(intensity=1.0, perturbations=[LatencyPerturbation(max_delay=2)])
    chaos.inject(state)
    assert state["current_time"] > 0