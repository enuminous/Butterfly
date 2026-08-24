from benchmark import layers, edges
from butterfly import compare_runs

if __name__ == "__main__":
    full = compare_runs(layers,edges,"L1",0.10,steps=8,deviation_threshold=0.02)
    no_feedback = compare_runs(
        layers,
        [e for e in edges if not e.feedback],
        "L1",
        0.10,
        steps=8,
        deviation_threshold=0.02
    )

    print("full amplification:",full["cross_layer_amplification"])
    print("no-feedback amplification:",no_feedback["cross_layer_amplification"])
    print("full boundary crossings:",full["boundary_crossings"])
    print("no-feedback boundary crossings:",no_feedback["boundary_crossings"])
