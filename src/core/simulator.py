"""
Simulator module

Este módulo implementa el núcleo del ciclo de simulación, encargado de:
- Gestionar la llegada y ejecución de procesos.
- Coordinar el scheduler y la inyección de caos.
- Recolectar métricas y manejar los estados de los procesos.

Uso:
    simulator = Simulator(scheduler, chaos_engine, metrics)
    simulator.load_processes(process_list)
    result = simulator.run_experiment(experiment)
"""

import logging

class Simulator:
    def __init__(self, scheduler, chaos_engine, metrics=None, logger=None):
        self.scheduler = scheduler
        self.chaos_engine = chaos_engine
        self.metrics = metrics
        self.logger = logger or logging.getLogger("simulator")
        self.time = 0
        self.processes = []
        self.arrival_queue = []
        self.ready_queue = []
        self.waiting_queue = []
        self.running_process = None
        self.completed = []

    def load_processes(self, process_list):
        self.processes = [p for p in process_list]
        self.arrival_queue = sorted(self.processes, key=lambda p: p.arrival_time)

    def tick(self):
        while self.arrival_queue and self.arrival_queue[0].arrival_time <= self.time:
            p = self.arrival_queue.pop(0)
            p.set_state("READY")
            self.ready_queue.append(p)
            self.scheduler.add_process(p)
            self.logger.debug(f"Process {p.pid} arrived and ready at time {self.time}")

        simulator_state = {
            "current_time": self.time,
            "ready_queue": self.ready_queue,
            "waiting_queue": self.waiting_queue,
            "running_process": self.running_process,
            "logger": self.logger
        }
        self.chaos_engine.inject(simulator_state)
        self.time = simulator_state["current_time"]

        if not self.running_process or getattr(self.running_process, "state", None) == "TERMINATED":
            self.running_process = self.scheduler.get_next_process(self.time)
            if self.running_process:
                self.running_process.set_state("RUNNING")
                if self.running_process.response_time is None:
                    self.running_process.response_time = self.time - self.running_process.arrival_time

        if self.running_process:
            self.running_process.remaining_time -= 1
            if self.running_process.remaining_time <= 0:
                self.running_process.set_state("TERMINATED")
                self.running_process.finish_time = self.time + 1
                self.metrics.record_process(self.running_process)
                self.completed.append(self.running_process)
                self.running_process = None

        self.metrics.cpu_utilization.append(1 if self.running_process else 0)
        self.time += 1

    def run_experiment(self, experiment):
        self.load_processes(experiment.processes)
        self.time = 0
        self.completed = []
        self.metrics.total_time = experiment.duration

        while self.time < experiment.duration and len(self.completed) < len(self.processes):
            self.tick()

        report = self.metrics.report()
        from src.core.simulation_result import SimulationResult
        return SimulationResult(report, self.completed, self.metrics)