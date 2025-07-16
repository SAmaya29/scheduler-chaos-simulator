# Chaos Scheduler Simulator

Simulador de planificación de procesos con ingeniería del caos para pruebas de resiliencia y robustez.

## 🚀 Instalación

```bash
git clone https://github.com/tuusuario/chaos_scheduler.git
cd chaos_scheduler
pip install -r requirements.txt
```

## 🛠️ Uso básico

```bash
python cli.py --algorithm round_robin --quantum 4 --workload high_cpu_bound --nprocs 10 --duration 100 --chaos latency memory_fault --intensity 0.3
```

## 🆕 Funcionalidades avanzadas

### Exportación de resultados

- **Exportar a CSV**:
  ```bash
  python cli.py ... --export-csv resultados.csv
  ```
- **Exportar a JSON**:
  ```bash
  python cli.py ... --export-json resultados.json
  ```

### Heatmap de utilización de recursos

- **Visualizar heatmap al final**:
  ```bash
  python cli.py ... --heatmap
  ```

### Modo simulación paso a paso visual

- **Ejecutar simulación paso a paso con visualización Gantt**:
  ```bash
  python cli.py --algorithm fcfs --workload mixed --nprocs 5 --duration 20 --step-by-step
  ```
  Pulsa Enter en cada tick para avanzar y ver el estado/visualización actual.

### Reporte de Fairness y Starvation

- El reporte por defecto muestra métricas avanzadas de fairness y starvation:
  ```
  fairness_index: 0.95
  starvation_count: 0
  ```

## 📂 Estructura del proyecto

```
chaos_scheduler/
├── src/
│   ├── core/                  # Núcleo del simulador y algoritmos
│   ├── chaos/                 # Motor y perturbaciones de caos
│   ├── metrics/               # Métricas y estadísticas
│   ├── visualization/         # Gráficas y dashboards
│   └── utils/                 # Utilidades y configuración
├── config/                    # Perfiles de experimento, workloads, caos
├── tests/                     # Unit, integration, chaos y performance tests
├── examples/                  # Ejemplos de experimentos y scripts
├── README.md
└── cli.py
```

## 🧪 Ejemplo de uso en Python

```python
from src.core.scheduler import ChaosScheduler
from src.chaos.chaos_engine import ChaosEngine
from src.metrics.statistics import Statistics
from src.core.simulator import Simulator
from src.core.experiment import Experiment
from src.utils.workload_generator import generate_workload
from src.chaos.perturbations.latency import LatencyPerturbation

processes = generate_workload("high_cpu_bound", 5, 50)
scheduler = ChaosScheduler(algorithm="round_robin", quantum=4)
chaos_engine = ChaosEngine(intensity=0.2, perturbations=[LatencyPerturbation()])
metrics = Statistics()
simulator = Simulator(scheduler, chaos_engine, metrics)
experiment = Experiment("high_cpu_bound", 50, "latency", processes)
results = simulator.run_experiment(experiment)
results.generate_report()
results.export_csv("resultados.csv")
results.export_json("resultados.json")
results.plot_metrics()
results.plot_heatmap()
```

## 📊 Visualización

El sistema genera gráficos de Gantt, métricas de CPU y heatmaps automáticamente.

## 🗂️ Configuración

- Parámetros por CLI o archivos YAML/JSON en `config/`.
- Perfiles de workload y caos predefinidos.

## 🧪 Testing

```bash
pytest tests/
```

---