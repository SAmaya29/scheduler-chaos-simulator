import random
import logging

class ChaosEngine:
    def __init__(self, intensity=0.1, perturbations=None, config=None):
        self.intensity = intensity
        self.perturbations = perturbations or []
        self.config = config or {}
        self.logger = logging.getLogger("chaos_engine")

    def inject(self, simulator_state):
        for perturbation in self.perturbations:
            if random.random() < self.intensity:
                self.logger.info(f"Injecting chaos: {perturbation.__class__.__name__}")
                perturbation.apply(simulator_state)