# 01 — Assembly Document
**Root:** `base_link` (pelvis/hip block). All other bodies hang off it as a strict kinematic tree.

| Sub-assembly | Links (in chain order) | Attaches to |
|---|---|---|
| Waist & torso | `torso_link` | `base_link` via `waist_yaw_joint` |
| Head | `neck_link` → `head_link` | `torso_link` via `neck_yaw_joint`, `head_pitch_joint` |
| Arm (×2) | `*_shoulder_link` → `*_shoulder_roll_link` → `*_upper_arm_link` → `*_forearm_link` → `*_hand_link` | `torso_link` |
| Hand (×2) | `*_hand_link` (rigid placeholder) | `*_forearm_link` via fixed `*_wrist_fixed_joint` |
| Leg (×2) | `*_hip_yaw_link` → `*_hip_roll_link` → `*_thigh_link` → `*_shank_link` → `*_ankle_link` → `*_foot_link` | `base_link` |

Small 40 mm blocks (`*_shoulder_link`, `*_hip_yaw_link`, `*_ankle_link`, etc.) represent **servo housings/brackets that sit between two axes** so each rotation has its own rigid body. Full tree: `docs/joint_hierarchy_tree.txt`.

## Recommended CAD assembly hierarchy (mirror this when organising the real CAD)
```
BHIV_Humanoid.asm
├─ 00_Pelvis            (= base_link)
├─ 01_Waist_Torso
├─ 02_Head_Neck
├─ 03_Arm_L / 03_Arm_R   (sub-asm per link above)
├─ 04_Hand_L / 04_Hand_R (placeholder)
└─ 05_Leg_L / 05_Leg_R
```
Rule: **one CAD sub-assembly = one URDF link**; **one mate/joint = one URDF joint**. Fasteners and wiring are excluded from the simulation export.

Exploded view and CAD-workspace screenshots: **not produced** (no CAD source supplied) — capture them once CAD is imported.
