# 07 — Simulation Readiness Checklist
Legend: ✅ done & evidenced · 🟡 placeholder, structure done · ❌ not done

| Item | Status | Evidence |
|---|---|---|
| Unique, consistent naming (`snake_case`, `_link`/`_joint`, `l_`/`r_`) | ✅ | `runtime_logs/validation_report.txt` |
| Single-root kinematic tree, no cycles/orphans | ✅ | validation report |
| Joint axes unit-length, limits present | ✅ | validation report |
| Left/right symmetry | ✅ | validation report |
| Inertial, visual and collision on every link | ✅ (placeholder values) | validation report |
| Joint orientation matches physical servos | ❌ | needs CAD/hardware check |
| Real dimensions & masses | 🟡 | A5 / M2 / M6 |
| DOF count verified against hardware | 🟡 | A1 / M3 |
| Mesh export (visual + simplified collision) | ❌ | no CAD supplied |
| `check_urdf` / RViz load | ❌ | not run here (no ROS2) |
| Simulator import proof (Isaac/Unreal/Gazebo) | ❌ | `deployment_proof/` empty |
| Self-collision matrix / actuator model / foot contact | ❌ | future work |
| CAD exploded view & workspace screenshots | ❌ | no CAD supplied |
