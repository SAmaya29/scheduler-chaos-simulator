import argparse
from src.core.scheduler import ChaosScheduler
from src.chaos.chaos_engine import ChaosEngine
from src.metrics.statistics import Statistics
from src.core.simulator import Simulator
from src.core.experiment import Experiment
from src.utils.workload_generator import generate_workload
from src.chaos.perturbations.latency import LatencyPerturbation
from src.chaos.perturbations.memory_fault import MemoryFaultPerturbation

def step_by_step_mode(simulator, experiment):
    print("\n=== Simulación paso a paso ===\n")
    simulator.load_processes(experiment.processes)
    simulator.time = 0
    simulator.completed = []
    simulator.metrics.total_time = experiment.duration

    from src.visualization.plots import plot_gantt

    while simulator.time < experiment.duration and len(simulator.completed) < len(simulator.processes):
        print(f"\n--- Tick {simulator.time} ---")
        print("Procesos en READY:", [p.pid for p in simulator.ready_queue])
        print("Procesos en WAITING:", [p.pid for p in simulator.waiting_queue])
        print("Proceso en CPU:", simulator.running_process.pid if simulator.running_process else "Ninguno")
        input("Presiona Enter para avanzar un tick...")
        simulator.tick()
        plot_gantt(simulator.completed + ([simulator.running_process] if simulator.running_process else []))
    print("\n=== Fin de la simulación ===")
    from src.core.simulation_result import SimulationResult
    results = SimulationResult(simulator.metrics.report(), simulator.completed, simulator.metrics)
    results.generate_report()
    return results

def main():
    parser = argparse.ArgumentParser(
        description="Chaos Scheduler Simulator - CLI"
    )
    parser.add_argument("--algorithm", type=str, default="round_robin", help="FCFS, SJF, round_robin, priority, multilevel_queue")
    parser.add_argument("--quantum", type=int, default=4, help="Quantum para Round Robin")
    parser.add_argument("--workload", type=str, default="high_cpu_bound", help="Tipo de carga de trabajo")
    parser.add_argument("--nprocs", type=int, default=10, help="Cantidad de procesos")
    parser.add_argument("--duration", type=int, default=100, help="Duración de la simulación (ticks)")
    parser.add_argument("--chaos", type=str, nargs="*", default=["latency"], help="Perturbaciones de caos a inyectar")
    parser.add_argument("--intensity", type=float, default=0.3, help="Intensidad del caos (0-1)")
    parser.add_argument("--debug", action="store_true", help="Modo debug")
    parser.add_argument("--no-gui", action="store_true", help="No mostrar gráficos")
    parser.add_argument("--export-csv", type=str, help="Archivo CSV para exportar resultados")
    parser.add_argument("--export-json", type=str, help="Archivo JSON para exportar resultados")
    parser.add_argument("--heatmap", action="store_true", help="Mostrar heatmap de uso de CPU por proceso al final")
    parser.add_argument("--step-by-step", action="store_true", help="Modo simulación paso a paso visual")

    args = parser.parse_args()

    # Setup logging
    import logging
    logging_level = "DEBUG" if args.debug else "INFO"
    from src.utils.logger import setup_logger
    setup_logger(logging_level)

    # Algoritmo scheduler
    scheduler_kwargs = {"quantum": args.quantum} if args.algorithm == "round_robin" else {}
    scheduler = ChaosScheduler(algorithm=args.algorithm, **scheduler_kwargs)

    # Perturbaciones de caos
    perturbation_map = {
        "latency": LatencyPerturbation(),
        "memory_fault": MemoryFaultPerturbation(),
        # Agrega más aquí si los implementas
    }
    chaos_perturbations = [perturbation_map[key] for key in args.chaos if key in perturbation_map]
    chaos_engine = ChaosEngine(intensity=args.intensity, perturbations=chaos_perturbations)

    # Generar procesos y lanzar
    processes = generate_workload(args.workload, args.nprocs, args.duration)
    metrics = Statistics()
    simulator = Simulator(scheduler, chaos_engine, metrics)
    experiment = Experiment(args.workload, args.duration, args.chaos, processes)

    # Modo paso a paso visual
    if args.step_by_step:
        results = step_by_step_mode(simulator, experiment)
    else:
        results = simulator.run_experiment(experiment)
        # Reporte con fairness y starvation
        print("==== Simulation Report ====")
        for k, v in results.metrics_report.items():
            print(f"{k}: {v}")

    # Exportación automática
    if args.export_csv:
        results.export_csv(args.export_csv)
        print(f"Resultados exportados a {args.export_csv}")
    if args.export_json:
        results.export_json(args.export_json)
        print(f"Resultados exportados a {args.export_json}")

    # Visualización
    if not args.no_gui:
        results.plot_metrics()
        if args.heatmap:
            results.plot_heatmap()

if __name__ == "__main__":
    main()