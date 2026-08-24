from dataclasses import dataclass
from typing import Dict, List
import copy

@dataclass
class Layer:
    state: float
    base: float = 0.0
    gain: float = 1.0
    threshold: float = 1.0

@dataclass
class Edge:
    source: str
    target: str
    weight: float
    feedback: bool = False

class ButterflySystem:
    def __init__(self, layers: Dict[str, Layer], edges: List[Edge]):
        self.layers = copy.deepcopy(layers)
        self.edges = list(edges)

    @staticmethod
    def clip(x, lo=0.0, hi=2.0):
        return max(lo, min(hi, x))

    def step(self):
        incoming = {k: 0.0 for k in self.layers}
        for e in self.edges:
            incoming[e.target] += e.weight * self.layers[e.source].state

        new_states = {}
        for name, layer in self.layers.items():
            # Mild nonlinearity after threshold to expose boundary amplification.
            nonlinear = 0.0
            if layer.state > layer.threshold:
                nonlinear = layer.gain * (layer.state - layer.threshold) ** 2
            new_states[name] = self.clip(layer.base + incoming[name] + nonlinear)

        for name, value in new_states.items():
            self.layers[name].state = value

        return {k: v.state for k, v in self.layers.items()}

    def run(self, steps=10):
        hist = [{k:v.state for k,v in self.layers.items()}]
        for _ in range(steps):
            hist.append(self.step())
        return hist

def compare_runs(layers, edges, source, delta, steps=10, deviation_threshold=0.05):
    ref = ButterflySystem(layers, edges)
    pert = ButterflySystem(layers, edges)
    pert.layers[source].state += delta

    ref_hist = ref.run(steps)
    pert_hist = pert.run(steps)

    names = list(layers)
    max_dev = {k:0.0 for k in names}
    boundary_crossings = 0

    for t in range(len(ref_hist)):
        for k in names:
            d = abs(pert_hist[t][k]-ref_hist[t][k])
            max_dev[k] = max(max_dev[k], d)

            th = layers[k].threshold
            ref_side = ref_hist[t][k] > th
            pert_side = pert_hist[t][k] > th
            if ref_side != pert_side:
                boundary_crossings += 1

    propagation_depth = sum(1 for d in max_dev.values() if d > deviation_threshold)
    total_dev = sum(max_dev.values())
    amplification = total_dev/(abs(delta)+1e-9)

    systemic = min(1.0, (
        0.35*min(1.0, amplification/5.0) +
        0.25*(propagation_depth/max(1,len(names))) +
        0.20*min(1.0,boundary_crossings/max(1,len(names))) +
        0.20*min(1.0,total_dev/max(1,len(names)))
    ))

    return {
        "initial_perturbation": delta,
        "max_deviation": max_dev,
        "propagation_depth": propagation_depth,
        "cross_layer_amplification": amplification,
        "boundary_crossings": boundary_crossings,
        "systemic_consequence": systemic,
        "reference_history": ref_hist,
        "perturbed_history": pert_hist
    }

def feedback_gain(layers, edges, source, delta, steps=10):
    full = compare_runs(layers, edges, source, delta, steps)
    no_fb_edges = [e for e in edges if not e.feedback]
    no_fb = compare_runs(layers, no_fb_edges, source, delta, steps)
    gain = full["cross_layer_amplification"]/(no_fb["cross_layer_amplification"]+1e-9)
    return gain
