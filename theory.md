# BUTTERFLY Theory

## 1. Problem

Complex systems often contain regions in which very small changes remain harmless, and other regions in which similarly small changes trigger large downstream consequences.

Relevant phenomena include:
- cascading configuration changes,
- threshold crossings,
- positive feedback,
- nonlinear amplification,
- policy or control regime changes,
- multi-layer dependency propagation,
- small local errors that become systemic.

BUTTERFLY evaluates this sensitivity explicitly.

## 2. Layered system

Let the system contain layers:

`L = {L_1, ..., L_n}`

Each layer has state:

`x_i(t)`

and receives influence from neighboring or linked layers.

## 3. Perturbation

Inject perturbation:

`delta_0`

at source layer `s`.

The perturbed trajectory is compared with an unperturbed reference trajectory.

## 4. Propagation

Let state difference at layer `i` and time `t` be:

`d_i(t) = |x_i^perturbed(t) - x_i^reference(t)|`

Propagation depth is the number of distinct layers where:

`d_i(t) > theta_i`

for at least one time step.

## 5. Amplification

Let initial perturbation magnitude be:

`P_0 = |delta_0|`

Let total downstream deviation be:

`P_T = sum_i w_i * max_t d_i(t)`

Cross-layer amplification:

`A = P_T / (P_0 + eps)`

## 6. Boundary crossing

Each layer may define operational boundaries:

`B_i = {b_i1, ..., b_ik}`

A boundary is crossed when the perturbed trajectory enters a regime that the reference trajectory does not.

Boundary-crossing count:

`C = number_of_unique_crossings`

## 7. Recursive feedback gain

If downstream layer `j` feeds back to upstream layer `i`, compare amplification with and without feedback.

`F = A_feedback / (A_no_feedback + eps)`

Values above 1 indicate recursive amplification.

## 8. Emergence score

A candidate emergent effect occurs when the global response is poorly explained by linear superposition of local effects.

Let expected additive response be:

`Y_linear`

and actual global response:

`Y_actual`

Then:

`E = |Y_actual - Y_linear| / (|Y_linear| + eps)`

## 9. Local/global yield ratio

If local change yields effect `Y_local` and system-wide effect is `Y_global`:

`R_yield = Y_global / (Y_local + eps)`

This captures disproportionate consequence.

## 10. EFMW interpretation

The EFMW-inspired element is recursive relational propagation across layers.

BUTTERFLY does not merely ask whether a perturbation changed the system.

It asks:
- where it traveled,
- which boundary it crossed,
- how feedback changed it,
- whether the global result became qualitatively different.

## 11. Falsifiable prediction

BUTTERFLY should add value in systems where:
- perturbations traverse multiple layers,
- nonlinear thresholds exist,
- feedback matters,
- local effects poorly predict global effects.

If standard sensitivity analysis and cascade models capture the same structure equally well, BUTTERFLY adds no justified complexity.
