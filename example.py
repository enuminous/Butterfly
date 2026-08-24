from butterfly import Layer, Edge, compare_runs

layers = {
    "input": Layer(0.5,base=0.2,threshold=0.8),
    "control": Layer(0.4,base=0.1,threshold=0.7),
    "network": Layer(0.3,base=0.1,threshold=0.65),
}

edges = [
    Edge("input","control",0.8),
    Edge("control","network",0.9),
]

print(compare_runs(
    layers,
    edges,
    source="input",
    delta=0.08,
    steps=6,
    deviation_threshold=0.02
))
