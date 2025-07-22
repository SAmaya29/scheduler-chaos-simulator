# 🌪️ Chaos Scheduler Simulator

<div align="center">

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/)
[![Coverage](https://img.shields.io/badge/coverage-85%25-yellowgreen.svg)](tests/)

**Simulador avanzado de planificación de procesos con ingeniería del caos para pruebas de resiliencia y robustez del sistema.**

[🚀 Instalación](#-instalación) •
[📖 Uso Rápido](#-uso-rápido) •
[🎯 Características](#-características) •
[📊 Ejemplos](#-ejemplos) •
[🧪 Testing](#-testing)

</div>

---

## 🎯 Características

### 🔧 Algoritmos de Scheduling
- **FCFS** (First Come First Served)
- **SJF** (Shortest Job First)
- **Round Robin** con quantum configurable
- **Priority Scheduling** (preemptive y non-preemptive)
- **Multilevel Queue** con múltiples niveles de prioridad

### 🌪️ Ingeniería del Caos
- **Latencia simulada** - Delays aleatorios en el sistema
- **Fallas de memoria** - Incremento dinámico de requerimientos
- **Sobrecarga de CPU** - Aumento inesperado del burst time
- **Interrupciones** - Procesos bloqueados aleatoriamente
- **Fallas de hardware** - Congelamiento temporal del scheduler

### 📈 Métricas Avanzadas
- Tiempo de espera promedio
- Tiempo de turnaround
- Utilización de CPU
- Throughput del sistema
- **Fairness index** con detección de starvation
- Análisis de distribución de recursos

### 🎨 Visualización
- **Gráficos de Gantt** interactivos
- **Heatmaps** de utilización de recursos
- **Métricas en tiempo real**
- **Simulación paso a paso** con visualización

---

## 🚀 Instalación

### Requisitos previos
- Python 3.8 o superior
- pip (administrador de paquetes)

### Instalación rápida
```bash
git clone https://github.com/SAmaya29/scheduler-chaos-simulator
cd scheduler-chaos-simulator
pip install -r requirements.txt
```

### Instalación para desarrollo
```bash
git clone https://github.com/SAmaya29/scheduler-chaos-simulator
cd scheduler-chaos-simulator
pip install -e .
pip install -r requirements-dev.txt
```

---

## 📖 Uso Rápido

### Simulación básica
```bash
python cli.py --algorithm round_robin --quantum 4 --workload mixed --nprocs 10 --duration 100
```

### Con ingeniería del caos
```bash
python cli.py --algorithm fcfs --workload high_cpu_bound --nprocs 15 --duration 200 \
  --chaos latency memory_fault cpu_overload --intensity 0.3
```

### Exportación completa
```bash
python cli.py --algorithm priority --workload mixed --nprocs 20 --duration 150 \
  --chaos interruption hardware_failure --intensity 0.4 \
  --export-csv resultados.csv --export-json resultados.json --heatmap
```

---

## 🆕 Funcionalidades Avanzadas

### 📊 Exportación de Resultados

<details>
<summary>Formatos de exportación disponibles</summary>

#### CSV
```bash
python cli.py [opciones] --export-csv resultados.csv
```
Genera archivo CSV con métricas detalladas por proceso.

#### JSON
```bash
python cli.py [opciones] --export-json resultados.json
```
Exporta resultados estructurados para análisis posterior.

</details>

### 🔥 Heatmap de Recursos

```bash
python cli.py [opciones] --heatmap
```
Genera visualización de calor mostrando utilización de CPU y memoria a lo largo del tiempo.

### 🎬 Simulación Paso a Paso

```bash
python cli.py --algorithm sjf --workload low_io_bound --nprocs 8 --duration 50 --step-by-step
```
**Controles interactivos:**
- `Enter`: Avanzar un tick
- `q`: Salir de la simulación
- `s`: Mostrar estadísticas actuales

---

## 📊 Ejemplos

### Ejemplo 1: Comparación de Algoritmos
```python
from src.core.scheduler import ChaosScheduler
from src.chaos.chaos_engine import ChaosEngine
from src.metrics.statistics import Statistics
from src.core.simulator import Simulator
from src.utils.workload_generator import generate_workload

# Generar carga de trabajo
processes = generate_workload("mixed", 15, 100)

# Configurar experimento
algorithms = ["fcfs", "sjf", "round_robin", "priority"]
results = {}

for alg in algorithms:
    scheduler = ChaosScheduler(algorithm=alg, quantum=4)
    chaos_engine = ChaosEngine(intensity=0.2, perturbations=[])
    metrics = Statistics()
    simulator = Simulator(scheduler, chaos_engine, metrics)
    
    result = simulator.run_experiment(processes)
    results[alg] = result.metrics_report
    
    print(f"{alg}: Wait Time = {result.metrics_report['avg_wait_time']:.2f}")
```

### Ejemplo 2: Análisis de Resiliencia
```python
from src.chaos.perturbations.latency import LatencyPerturbation
from src.chaos.perturbations.memory_fault import MemoryFaultPerturbation

# Configurar diferentes niveles de caos
chaos_levels = [0.1, 0.3, 0.5, 0.7]
perturbations = [LatencyPerturbation(), MemoryFaultPerturbation()]

for intensity in chaos_levels:
    chaos_engine = ChaosEngine(intensity=intensity, perturbations=perturbations)
    # ... ejecutar simulación
    print(f"Caos {intensity}: Throughput = {result.throughput:.2f}")
```

### Ejemplo 3: Experimento Personalizado
```python
from src.core.experiment import Experiment

# Crear experimento con configuración específica
experiment = Experiment(
    name="High Load Stress Test",
    workload_type="high_cpu_bound",
    process_count=50,
    duration=500,
    chaos_intensity=0.4,
    algorithm="multilevel_queue"
)

results = simulator.run_experiment(experiment)
results.generate_report()
results.export_csv("stress_test_results.csv")
results.plot_heatmap()
```

### Ejemplo 4: Uso general
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

---

## 📂 Arquitectura del Proyecto

```
chaos_scheduler/
├── 🎯 src/core/              # Núcleo de la simulación
│   ├── process.py           # Definición de procesos
│   ├── scheduler.py         # Factory de schedulers
│   ├── simulator.py         # Motor de simulación
│   ├── experiment.py        # Configuración de experimentos
│   ├── simulation_result.py # Resultados y reportes
│   └── algorithms/          # Algoritmos de scheduling
├── 🌪️ src/chaos/            # Sistema de ingeniería del caos
│   ├── chaos_engine.py      # Motor de inyección de caos
│   └── perturbations/       # Tipos de perturbaciones
├── 📈 src/metrics/          # Métricas y estadísticas
├── 🎨 src/visualization/    # Gráficos y visualización
├── 🛠️ src/utils/           # Utilidades y configuración
├── ⚙️ config/              # Configuración y perfiles
├── 🧪 tests/               # Suite de pruebas
├── 📝 examples/            # Ejemplos de uso
└── 📱 cli.py               # Interfaz de línea de comandos
```

---

## 🧪 Testing

### Ejecutar todas las pruebas
```bash
pytest tests/ -v
```

### Pruebas específicas
```bash
# Unit tests
pytest tests/test_fcfs.py -v

# Integration tests
pytest tests/test_simulator.py -v

# Performance tests
pytest tests/test_performance.py -v

# Chaos tests
pytest tests/test_chaos_engine.py -v
```

### Cobertura de código
```bash
pytest --cov=src tests/
```

---

## ⚙️ Configuración Avanzada

### Archivos de configuración
- `config/default.yaml`: Configuración por defecto
- `config/workloads/`: Perfiles de carga de trabajo
- `config/chaos_profiles/`: Perfiles de caos predefinidos

### Ejemplo de configuración personalizada
```yaml
# config/custom_experiment.yaml
scheduler:
  algorithm: "round_robin"
  quantum: 6

chaos:
  intensity: 0.25
  perturbations:
    - type: "latency"
      max_delay: 5
    - type: "memory_fault"
      fault_probability: 0.1

workload:
  type: "mixed"
  process_count: 25
  duration: 300
```

### Usar configuración personalizada
```bash
python cli.py --config config/custom_experiment.yaml
```

---

## 🤝 Contribución

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre** un Pull Request

### Convenciones de código
- Seguir PEP 8
- Agregar docstrings a todas las funciones
- Mantener cobertura de tests > 80%
- Usar type hints donde sea posible

---


## 👥 Autores

- **Sebastian Amaya Perez** - *Desarrollo inicial* - [SAmaya29](https://github.com/SAmaya29)

---

## 🙏 Agradecimientos

- Inspirado en principios de ingeniería del caos de Netflix
- Algoritmos de scheduling basados en literatura de sistemas operativos
- Comunidad de código abierto por las librerías utilizadas

---

<div align="center">

**¿Te gustó el proyecto? ¡Dale una ⭐ en GitHub!**

[🐛 Reportar Bug](https://github.com/tuusuario/chaos_scheduler/issues) •
[💡 Solicitar Feature](https://github.com/tuusuario/chaos_scheduler/issues) •
[💬 Discusiones](https://github.com/tuusuario/chaos_scheduler/discussions)

</div>
