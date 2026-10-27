# Handover — read this if you have no prior context
**What this is:** the structural foundation of a digital twin for the BHIV Humanoid. Structure/naming/tooling are solid; numbers are placeholders.
**Do first (≈1–2 h):**
1. Put the real CAD in `cad_source/`; get the hardware revision (M1).
2. Count the actual servos/DOF; compare with `docs/03_dof_map.md`. Edit `tools/generate.py` where they differ.
3. Replace link sizes, masses, joint origins with CAD measurements; update limits from physical hard-stops.
4. `python3 tools/generate.py && python3 tools/validate.py` — must print ALL PASS.
5. On a ROS2 machine run `check_urdf` and RViz; sweep each joint and fix any wrong axis direction.
6. Export meshes, capture the missing screenshots, update `07_simulation_readiness_checklist.md` honestly.
**Don't:** redesign geometry, rename links/joints casually (names are referenced across docs), or mark items ✅ without evidence.
**Contacts:** Mechanical (dimensions), Electronics (servo placement reference only), Unreal/Simulation (target requirements).
