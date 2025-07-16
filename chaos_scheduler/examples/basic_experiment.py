from src.core.scheduler import ChaosScheduler
from src.chaos.chaos_engine import ChaosEngine
from src.metrics.statistics import Statistics
from src.core.simulator import Simulator
from src.core.experiment import Experiment
from src.utils.workload_generator import generate_workload
from src.chaos.perturbations.latency import LatencyPerturbation
from src.chaos.perturbations.memory_fault import MemoryFaultPerturbation

if __name__ == "__main__":
    # Configuración
    processes = generate_workload("high_cpu_bound", 10, 100)
    scheduler = ChaosScheduler(algorithm="round_robin", quantum=4)
    chaos_engine = ChaosEngine(
        intensity=0.3,
        perturbations=[
            LatencyPerturbation(max_delay=3),
            MemoryFaultPerturbation()
        ]
    )
    metrics = Statistics()
    simulator = Simulator(scheduler, chaos_engine, metrics)

    experiment = Experiment(
        workload="high_cpu_bound",
        duration=100,
        chaos_config="moderate_chaos",
        processes=processes
    )

    results = simulator.run_experiment(experiment)
    results.generate_report()
    results.plot_metrics()