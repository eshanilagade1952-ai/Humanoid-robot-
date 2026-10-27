# 06 — Assumptions & Missing Information

## Assumptions (all unverified)
| ID | Assumption | Impact if wrong |
|---|---|---|
| A1 | 23 DOF: waist 1, head 2, arm 4×2, leg 6×2, hands fixed | DOF map, URDF joints, servo table change |
| A2 | Every DOF is one servo, single axis | Linkage-driven joints need mimic/transmission modelling |
| A3 | Pelvis (`base_link`) is the root; zero pose = arms down, legs straight | Re-parenting if CAD root differs |
| A4 | Joint limits (rad) are generic servo-humanoid values | Unsafe/limited motion in sim vs. reality |
| A5 | Box geometry and masses (~8 kg total) are stand-ins; inertia from solid-box formula | Dynamics, balance and control tuning invalid until replaced |
| A6 | Servo channel IDs S01–S23 are logical placeholders in joint order | Must be replaced with real servo IDs from Electronics |
| A7 | Hand is a rigid block; neck has yaw+pitch only | Add finger/wrist DOF later |
| A8 | Same joint axes on left/right (sign handled in controller) | Flip if CAD mates are mirrored |

## Missing information (needs owners)
| # | Needed | Owner |
|---|---|---|
| M1 | Existing CAD files and **final hardware revision** | Mechanical |
| M2 | Real link dimensions, joint origins, total height/mass | Mechanical |
| M3 | Actual DOF count and servo model per joint (torque, range, speed) | Mechanical / Electronics |
| M4 | Servo mounting positions & horn orientation | Electronics (reference only) |
| M5 | Mechanical hard-stops / true joint ranges | Mechanical |
| M6 | Per-part mass, COM, material | Mechanical |
| M7 | Target simulator & version (Isaac Sim / Unreal / Gazebo) | Simulation Team |
| M8 | Foot geometry and ground-contact requirements | Mechanical / Simulation |
