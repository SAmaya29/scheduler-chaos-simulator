from src.core.scheduler import ChaosScheduler
from src.chaos.chaos_engine import ChaosEngine
from src.metrics.statistics import Statistics
from src.core.simulator import Simulator
from src.core.experiment import Experiment
from src.utils.workload_generator import generate_workload
from src.chaos.perturbations.latency import LatencyPerturbation

def compare_algorithms():
    processes = generate_workload("mixed", 15, 80)
    configs = [
        {"name": "Sin caos", "chaos": []},
        {"name": "Con Latency", "chaos": [LatencyPerturbation()]},
    ]
    for conf in configs:
        print("===", conf["name"], "===")
        scheduler = ChaosScheduler(algorithm="fcfs")
        chaos_engine = ChaosEngine(intensity=0.3, perturbations=conf["chaos"])
        metrics = Statistics()
        simulator = Simulator(scheduler, chaos_engine, metrics)
        experiment = Experiment("mixed", 80, conf["name"], processes)
        results = simulator.run_experiment(experiment)
        results.generate_report()
        print()

if __name__ == "__main__":
    compare_algorithms()