# BUTTERFLY: Boundary-Under-Test Transition, Emergence and Recursive Feedback across Layered Yield

## Abstract

BUTTERFLY is an experimental framework for evaluating how small perturbations propagate through layered systems, cross operational boundaries, amplify through recursive feedback, and generate system-level consequences disproportionate to their local magnitude.

## 1. Motivation

Not all small changes are equal.

In highly coupled systems, a minor perturbation may:
- remain local,
- spread weakly,
- cross one or more thresholds,
- enter a feedback loop,
- or trigger a qualitatively different global regime.

BUTTERFLY is designed to distinguish these cases.

## 2. Model

Layer deviation:

`d_i(t)=|x_i^perturbed(t)-x_i^reference(t)|`

Propagation depth:

`P=number of layers with max_t d_i(t)>theta_i`

Amplification:

`A=sum_i w_i max_t d_i(t) / |delta_0|`

Boundary crossing:

`C=count of perturbed-only regime transitions`

Feedback gain:

`F=A_feedback/A_no_feedback`

Emergence:

`E=|Y_actual-Y_linear|/(|Y_linear|+eps)`

## 3. Metrics

- perturbation sensitivity
- propagation depth
- cross-layer amplification
- boundary crossings
- feedback gain
- emergence score
- local/global yield ratio
- systemic consequence

## 4. Baselines

- local sensitivity analysis
- Jacobian-based perturbation analysis
- Monte Carlo perturbation tests
- cascade models
- graph propagation
- nonlinear dynamical simulation

## 5. Ablations

- remove feedback edges
- remove nonlinear thresholds
- single-layer evaluation
- linearized dynamics only
- no boundary-crossing term
- no propagation-depth term

## 6. Falsification

If conventional sensitivity, cascade, and nonlinear dynamics methods predict held-out system responses equally well under matched information and compute, BUTTERFLY's added formulation is not justified.

## 7. Zoo II closure

BUTTERFLY closes the second 23-animal ring because it tests what happens when all the prior ideas—memory, context, dependency, adaptation, coordination, robustness, recovery, and emergence—are connected strongly enough that a local change can become a global event.

## 8. Claim boundary

BUTTERFLY measures model sensitivity and propagation. It does not establish literal chaos, catastrophe, or real-world causation without external validation.
