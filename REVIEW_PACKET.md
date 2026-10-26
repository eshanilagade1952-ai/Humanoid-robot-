# REVIEW_PACKET — Humanoid Digital Twin → ROS & Simulation Validation (Task 2)
Date: 2026-10-12 | Owner: Eshani | State: WORKING | Convergence: PARTIALLY CONVERGED

## Result in one line
The pipeline URDF → check_urdf → robot_state_publisher → RViz → joint states → visible motion → Gazebo import was run and recorded. Correspondence to the real BHIV Humanoid is UNKNOWN because the real CAD/design files were not provided.

## Chain status
| Step | Status | Evidence |
|---|---|---|
| Actual design reviewed | NOT DONE | no CAD, dimensions or handover material received |
| DOF reconciliation | PARTIAL | docs/reconciliation_matrix.md (real values UNKNOWN) |
| URDF corrected from real geometry | NOT DONE | blocked on CAD; Task 1 placeholder URDF used unchanged |
| URDF validation | DONE | evidence_packet/validation/ (check_urdf + validate.py, 14/14 PASS) |
| ROS 2 + robot_state_publisher + RViz | DONE | screenshots/, runtime_logs/ros_nodes.txt, joint_states_sample.txt |
| Joint motion in RViz | DONE | video in simulation_proof/ |
| TF tree | DONE | simulation_proof/frames_*.pdf |
| Simulator import (Gazebo) | DONE (with limits) | runtime_logs/gazebo_*.txt, screenshots/, video in simulation_proof/ |

## Gazebo details
- Attempt 1 crashed at startup: OGRE GL3Plus UnimplementedException on WSL graphics (log: gazebo_launch.txt), before the robot was loaded.
- Attempt 2 (software rendering, ogre engine) ran. The URDF spawned as bhiv_humanoid and is visible in the Entity Tree and the 3D view (video recorded).
- The display flickers under software rendering. The model has no controller, so stable standing is not expected.

## Known gaps
1. Real CAD, dimensions, masses, servo data and the final hardware revision were not provided.
2. All sizes, limits and the 23-DOF count are Task 1 placeholders.
3. Boxes are used instead of CAD meshes, so there is no mesh package.
4. Joint directions were not checked against physical servos.
5. No colours, controller or self-collision matrix.

## Out of scope (per task)
Hardware fabrication, servo control, safety-layer execution, physical actuation.

## Reviewer ask
Provide the CAD files and final hardware revision so the matrix can be completed and real meshes added.
