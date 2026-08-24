# Propagation Model

## Layer schema

```json
{
  "id": "L2",
  "state": 0.42,
  "gain": 0.8,
  "threshold": 0.7
}
```

## Edge schema

```json
{
  "source": "L1",
  "target": "L2",
  "weight": 0.35,
  "feedback": false
}
```

## Reference update

A simple reference dynamics:

`x_j(t+1) = clip(base_j + sum_i w_ij*x_i(t) + nonlinear_j(x_j))`

## Perturbed run

Clone the same system and apply `delta_0` to one source state.

## Metrics

- max layer deviation
- propagation depth
- total deviation
- amplification
- boundary crossing
- feedback gain
- emergence score

## Boundary definition

The reference implementation treats a threshold crossing as a boundary event.

More advanced deployments may define:
- categorical regimes,
- safety envelopes,
- policy state transitions,
- attractor transitions.
