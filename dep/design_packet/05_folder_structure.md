# 05 — Folder Structure
```
bhiv_humanoid_digital_twin/
├─ README.md  REVIEW_PACKET.md
├─ cad_source/                  # ← put existing CAD (STEP/F3D/SLDASM) here, untouched
├─ urdf/                        # bhiv_humanoid_foundation.urdf (later: meshes/, xacro/)
├─ config/model_params.json
├─ tools/                       # generate.py, validate.py
├─ docs/                        # 01–08 + HANDOVER + joint_hierarchy_tree.txt
├─ evidence_packet/
│  ├─ review_packet.md
│  ├─ screenshots/              # preview render, hierarchy text; add CAD screenshots here
│  ├─ code_packet/              # URDF + scripts snapshot
│  ├─ runtime_logs/             # validation_report.txt, check_urdf_NOT_RUN.txt
│  └─ deployment_proof/         # empty until a sim import is actually done
└─ dep/                         # Daily Engineering Packet
```
Planned additions: `urdf/meshes/visual/*.stl`, `urdf/meshes/collision/*.stl`, `urdf/xacro/`, `sim/isaac/`, `sim/unreal/`.
