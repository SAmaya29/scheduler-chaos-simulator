from src.core.scheduler import ChaosScheduler
from src.chaos.chaos_engine import ChaosEngine
from src.metrics.statistics import Statistics
from src.core.simulator import Simulator
from src.core.experiment import Experiment
from src.utils.workload_generator import generate_workload
from src.chaos.perturbations.latency import LatencyPerturbation

def test_simulation_run():
    processes = generate_workload("high_cpu_bound", 5, 20)
    scheduler = ChaosScheduler(algorithm="fcfs")
    chaos_engine = ChaosEngine(intensity=0.0, perturbations=[])
    metrics = Statistics()
    simulator = Simulator(scheduler, chaos_engine, metrics)
    experiment = Experiment("high_cpu_bound", 20, "none", processes)
    results = simulator.run_experiment(experiment)
    assert len(results.completed_processes) > 0
    assert "avg_wait_time" in results.metrics_report