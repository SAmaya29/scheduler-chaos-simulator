# Chaos Scheduler Simulator

---

## ✨ Tabla de Contenidos

- [🚀 Instalación](#-instalaci%C3%B3n)
- [🛠%ef%b8%8f Uso básico](#%ef%b8%8f-uso-b%C3%A1sico)
- [🌟 Funcionalidades avanzadas](#-funcionalidades-avanzadas)
  - [Exportación de resultados](#exportaci%C3%B3n-de-resultados)
  - [Visualización: heatmap y Gantt](#visualizaci%C3%B3n-heatmap-y-gantt)
  - [Reporte de fairness y starvation](#reporte-de-fairness-y-starvation)
- [📚 Ejemplos de uso en Python](#-ejemplos-de-uso-en-python)
- [🔧 Configuración](#-configuraci%C3%B3n)
- [💡 Arquitectura del sistema](#-arquitectura-del-sistema)
- [🧰 Testing](#-testing)
- [💪 Contribución](#-contribuci%C3%B3n)
- [📟 Comunidad y agradecimientos](#-comunidad-y-agradecimientos)

---

## 🚀 Instalación

```bash
# Clona el repositorio
git clone https://github.com/tuusuario/chaos_scheduler.git
cd chaos_scheduler

# Instala las dependencias
pip install -r requirements.txt
```

---

## 🛠%ef%b8%8f Uso básico

```bash
python cli.py \
  --algorithm round_robin \
  --quantum 4 \
  --workload high_cpu_bound \
  --nprocs 10 \
  --duration 100 \
  --chaos latency memory_fault \
  --intensity 0.3
```

---

## 🌟 Funcionalidades avanzadas

```bash
# Exportar a CSV
python cli.py ... --export-csv resultados.csv

# Exportar a JSON
python cli.py ... --export-json resultados.json
```

```bash
# Visualizar heatmap de utilización de CPU
python cli.py ... --heatmap

# Modo paso a paso visual con Gantt
python cli.py \
  --algorithm fcfs \
  --workload mixed \
  --nprocs 5 \
  --duration 20 \
  --step-by-step
```

Pulsa Enter en cada tick para avanzar.

Se generan al finalizar:

```
fairness_index: 0.95
starvation_count: 0
```

---

## 📚 Ejemplos de uso en Python

```python
from src.core.scheduler import ChaosScheduler
from src.chaos.chaos_engine import ChaosEngine
from src.metrics.statistics import Statistics
from src.core.simulator import Simulator
from src.core.experiment import Experiment
from src.utils.workload_generator import generate_workload
from src.chaos.perturbations.latency import LatencyPerturbation

# Generar procesos
tasks = generate_workload("high_cpu_bound", 5, 50)

# Inicializar componentes
scheduler = ChaosScheduler(algorithm="round_robin", quantum=4)
chaos_engine = ChaosEngine(intensity=0.2, perturbations=[LatencyPerturbation()])
metrics = Statistics()
simulator = Simulator(scheduler, chaos_engine, metrics)

# Ejecutar experimento
experiment = Experiment("high_cpu_bound", 50, "latency", tasks)
results = simulator.run_experiment(experiment)

# Salida y visualización
results.generate_report()
results.export_csv("resultados.csv")
results.export_json("resultados.json")
results.plot_metrics()
results.plot_heatmap()
```

---

## 🔧 Configuración

Puedes personalizar desde la CLI o usando archivos en `config/`:

**Ejemplo de archivo YAML (**\`\`**)**:

```yaml
algorithm: round_robin
quantum: 3
workload: mixed
nprocs: 8
duration: 100
chaos:
  intensity: 0.4
  types:
    - latency
    - cpu_overload
```

---

## 💡 Arquitectura del sistema

```text
chaos_scheduler/
├── src/
│   ├── core/          # Lógica del planificador y simulación
│   ├── chaos/         # Inyección de fallos y perturbaciones
│   ├── metrics/       # Cálculo de fairness y estadísticas
│   ├── visualization/ # Heatmaps, Gantt y gráficas
│   └── utils/         # Config, logger y generadores
├── config/            # Archivos YAML de configuración
├── tests/             # Pytests para cada módulo
├── examples/          # Scripts ilustrativos
└── cli.py             # Interfaz principal de ejecución
```

---

## 🧰 Testing

Ejecuta los tests:

```bash
pytest tests/
```

Opcionalmente:

```bash
pytest tests/test_fcfs.py -v
pytest --cov=src/ tests/
```

---

## 💪 Contribución

1. Haz un fork del proyecto
2. Crea tu rama `feature/mi-mejora`
3. Asegura que pase `pytest`
4. Abre un Pull Request con tu propuesta

---

## 📟 Comunidad y agradecimientos

Este proyecto está inspirado en la necesidad de probar algoritmos de planificación en condiciones de fallo.

Agradecimientos especiales a:

- [OSTEP](http://pages.cs.wisc.edu/~remzi/OSTEP/)
- Comunidad de Python Colombia

---

