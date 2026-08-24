from butterfly import Layer, Edge, compare_runs, feedback_gain

layers = {
    "L1": Layer(state=0.40, base=0.20, gain=1.0, threshold=0.75),
    "L2": Layer(state=0.35, base=0.15, gain=1.2, threshold=0.70),
    "L3": Layer(state=0.30, base=0.10, gain=1.4, threshold=0.65),
    "L4": Layer(state=0.25, base=0.10, gain=1.6, threshold=0.60),
}

edges = [
    Edge("L1","L2",0.90),
    Edge("L2","L3",0.95),
    Edge("L3","L4",1.00),
    Edge("L4","L2",0.35,feedback=True),
]

if __name__ == "__main__":
    for delta in [0.01,0.05,0.10,0.20]:
        out = compare_runs(layers,edges,"L1",delta,steps=8,deviation_threshold=0.02)
        out["feedback_gain"] = feedback_gain(layers,edges,"L1",delta,steps=8)
        print({
            "delta":delta,
            "propagation_depth":out["propagation_depth"],
            "amplification":out["cross_layer_amplification"],
            "boundary_crossings":out["boundary_crossings"],
            "feedback_gain":out["feedback_gain"],
            "systemic_consequence":out["systemic_consequence"]
        })
