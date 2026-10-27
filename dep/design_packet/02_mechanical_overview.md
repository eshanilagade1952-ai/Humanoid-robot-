# 02 — Mechanical Overview (foundation model, placeholder values)
- **Architecture:** servo-driven biped humanoid, single kinematic tree, ~1.0 m tall in the placeholder model, ~8.0 kg total placeholder mass.
- **Kinematic layout:** 1 waist yaw · 2 neck/head · 4 per arm · 6 per leg = **23 DOF**. Hands are rigid placeholders.
- **Joint types:** all actuated joints are single-axis revolute (one servo each). Multi-axis hip/shoulder/ankle joints are modelled as **stacked single-axis joints with zero-length intermediate links**, which is how servo humanoids are physically built and keeps URDF valid.
- **Axis convention at zero pose (arms down, legs straight, facing +X):** yaw = Z, pitch = Y, roll = X. Left and right sides use the **same axis vectors**; mirrored servos therefore need a sign flip in the controller, not a different URDF axis.
- **Mechanical constraints modelled:** joint limits (rad), rigid parent-child mounting, box collision geometry. **Not modelled yet:** servo torque/speed curves, gear backlash, self-collision matrix, cable routing, foot contact parameters.
- **Placeholder dimensions (m):** thigh 0.20, shank 0.20, upper arm 0.12, forearm 0.11, hip width 0.14 (±0.07), shoulder width 0.28 (±0.14), foot 0.16×0.07.
