# DOF / Joint Reconciliation Matrix (Task 2, Day 1)

Status legend: CONFIRMED / UNKNOWN / NEEDS CORRECTION.
The real BHIV Humanoid CAD/design files were NOT provided, so every comparison with the real robot is UNKNOWN. No values were invented.

## A. Structure and software checks

| Item | Task 1 / URDF value | Real robot value | Status | Note |
|---|---|---|---|---|
| Total DOF | 23 (estimated) | not available | UNKNOWN | needs servo count from Mechanical |
| Root link | base_link (pelvis) | not available | UNKNOWN | |
| Hand DOF | 0 (rigid block) | not available | UNKNOWN | placeholder per Task 1 |
| Link dimensions | placeholder boxes | not available | UNKNOWN | needs CAD |
| Link masses | placeholders (~8 kg total) | not available | UNKNOWN | needs CAD |
| Servo models / IDs | S01-S23 placeholders | not available | UNKNOWN | Electronics reference only |
| URDF validity (check_urdf, validate.py) | PASS | n/a (software check) | CONFIRMED | proves file validity, not real-robot match |
| Kinematic tree loads in ROS 2 (26 links, 25 joints) | loads, TF tree generated | n/a (software check) | CONFIRMED | see simulation_proof/frames_*.pdf |
| Joints move in RViz | 23 sliders, motion recorded | n/a (software check) | CONFIRMED | see video in simulation_proof |
| Imports into Gazebo | spawned with software rendering | n/a (software check) | CONFIRMED | see gazebo logs, screenshots, video |

## B. Per-joint matrix

| Joint | Task 1 value (axis, limits, origin) | Real robot value | Status |
|---|---|---|---|
| `waist_yaw_joint` | Z (yaw), limits -1.57 to 1.57 rad, origin [0, 0, 0.04] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `neck_yaw_joint` | Z (yaw), limits -1.57 to 1.57 rad, origin [0, 0, 0.25] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `head_pitch_joint` | Y (pitch), limits -0.7 to 0.7 rad, origin [0, 0, 0.04] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `l_shoulder_pitch_joint` | Y (pitch), limits -2.5 to 2.5 rad, origin [0, 0.14, 0.21] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `l_shoulder_roll_joint` | X (roll), limits -1.57 to 1.57 rad, origin [0, 0, 0] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `l_upper_arm_yaw_joint` | Z (yaw), limits -1.57 to 1.57 rad, origin [0, 0, -0.03] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `l_elbow_pitch_joint` | Y (pitch), limits -2.4 to 0.0 rad, origin [0, 0, -0.12] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `l_hip_yaw_joint` | Z (yaw), limits -0.8 to 0.8 rad, origin [0, 0.07, -0.04] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `l_hip_roll_joint` | X (roll), limits -0.7 to 0.7 rad, origin [0, 0, -0.03] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `l_hip_pitch_joint` | Y (pitch), limits -1.57 to 0.8 rad, origin [0, 0, -0.02] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `l_knee_pitch_joint` | Y (pitch), limits 0.0 to 2.4 rad, origin [0, 0, -0.2] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `l_ankle_pitch_joint` | Y (pitch), limits -0.8 to 0.8 rad, origin [0, 0, -0.2] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `l_ankle_roll_joint` | X (roll), limits -0.5 to 0.5 rad, origin [0, 0, -0.02] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `r_shoulder_pitch_joint` | Y (pitch), limits -2.5 to 2.5 rad, origin [0, -0.14, 0.21] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `r_shoulder_roll_joint` | X (roll), limits -1.57 to 1.57 rad, origin [0, 0, 0] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `r_upper_arm_yaw_joint` | Z (yaw), limits -1.57 to 1.57 rad, origin [0, 0, -0.03] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `r_elbow_pitch_joint` | Y (pitch), limits -2.4 to 0.0 rad, origin [0, 0, -0.12] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `r_hip_yaw_joint` | Z (yaw), limits -0.8 to 0.8 rad, origin [0, -0.07, -0.04] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `r_hip_roll_joint` | X (roll), limits -0.7 to 0.7 rad, origin [0, 0, -0.03] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `r_hip_pitch_joint` | Y (pitch), limits -1.57 to 0.8 rad, origin [0, 0, -0.02] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `r_knee_pitch_joint` | Y (pitch), limits 0.0 to 2.4 rad, origin [0, 0, -0.2] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `r_ankle_pitch_joint` | Y (pitch), limits -0.8 to 0.8 rad, origin [0, 0, -0.2] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |
| `r_ankle_roll_joint` | X (roll), limits -0.5 to 0.5 rad, origin [0, 0, -0.02] m | NOT AVAILABLE (CAD not provided) | UNKNOWN |

## C. NEEDS CORRECTION (from RViz observation)

None confirmed yet. Add any joint here that moved in a wrong direction.

Note: joint limits and axis directions are Task 1 assumptions and must be checked against the physical servos.
