import time
from src.core.scheduler import ChaosScheduler
from src.chaos.chaos_engine import ChaosEngine
from src.metrics.statistics import Statistics
from src.core.simulator import Simulator
from src.core.experiment import Experiment
from src.utils.workload_generator import generate_workload

def test_performance_large_run():
    processes = generate_workload("high_cpu_bound", 100, 500)
    scheduler = ChaosScheduler(algorithm="fcfs")
    chaos_engine = ChaosEngine(intensity=0.1, perturbations=[])
    metrics = Statistics()
    simulator = Simulator(scheduler, chaos_engine, metrics)
    experiment = Experiment("high_cpu_bound", 500, "none", processes)
    t0 = time.time()
    results = simulator.run_experiment(experiment)
    t1 = time.time()
    assert t1 - t0 < 10  # El run no debe durar más de 10 segundos