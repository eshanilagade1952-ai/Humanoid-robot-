# BHIV Humanoid — Digital Twin Foundation 

A documented, simulation-ready **digital foundation** for the BHIV Humanoid: structured URDF, DOF/joint maps, validation tooling, and handover docs. No hardware changes, no cosmetic redesign.

> **STATUS: PARTIALLY CONVERGED.** The original Humanoid CAD and measured dimensions were not available when this foundation was built. Kinematic *structure, naming and hierarchy* are production-ready; **all dimensions, masses, limits and the 23-DOF count are placeholders** that must be reconciled against the real CAD (see `docs/06_assumptions_and_missing_info.md`). Nothing here claims to be measured data.

## Quick start
```bash
python3 tools/generate.py     # regenerates URDF, DOF map, joint map, preview from one parameter set
python3 tools/validate.py     # 14 structural/simulation-readiness checks
check_urdf urdf/bhiv_humanoid_foundation.urdf   # needs ROS2 / liburdfdom-tools (NOT yet run)
```
To adopt real dimensions: edit the numbers in `tools/generate.py` (links `L(...)` and joint origins `J(...)`), regenerate, validate.

## Contents
| Path | Purpose |
|---|---|
| `urdf/bhiv_humanoid_foundation.urdf` | 26 links, 25 joints (23 revolute + 2 fixed hand mounts) |
| `tools/generate.py`, `tools/validate.py` | Single-source generator + readiness validator |
| `config/model_params.json` | Machine-readable link/joint parameters |
| `docs/01…08_*.md`, `docs/HANDOVER.md` | Assembly, mechanical, DOF, joints, folders, assumptions, checklist, sim recommendations, handover |
| `cad_source/` | **Empty on purpose** — drop the existing CAD/STEP/F3D files here |
| `evidence_packet/` | Review packet, preview image, validation log, code copy |
| `dep/` | Daily Engineering Packet |
| `REVIEW_PACKET.md` | Reviewer summary |

## Conventions
REP-103 frames (x forward, y left, z up), SI units, `snake_case`, links end `_link`, joints end `_joint`, side prefix `l_` / `r_`. Joint frame = child link frame at joint axis origin.
