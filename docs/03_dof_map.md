# DOF Map (ESTIMATED — see 06_assumptions_and_missing_info.md)

| Region | DOF |
|---|---|
| waist | 1 |
| head | 2 |
| arm | 6 |
| forearm | 2 |
| leg | 8 |
| foot | 4 |
| **Total** | **23** |

## Per-joint

| # | Servo ch. (placeholder) | Joint | Parent → Child | Axis | Limits (rad) | Body region |
|---|---|---|---|---|---|---|
| 1 | S01 | `waist_yaw_joint` | base_link → torso_link | Z (yaw) | -1.57 … 1.57 | waist |
| 2 | S02 | `neck_yaw_joint` | torso_link → neck_link | Z (yaw) | -1.57 … 1.57 | head |
| 3 | S03 | `head_pitch_joint` | neck_link → head_link | Y (pitch) | -0.7 … 0.7 | head |
| 4 | S04 | `l_shoulder_pitch_joint` | torso_link → l_shoulder_link | Y (pitch) | -2.5 … 2.5 | arm |
| 5 | S05 | `l_shoulder_roll_joint` | l_shoulder_link → l_shoulder_roll_link | X (roll) | -1.57 … 1.57 | arm |
| 6 | S06 | `l_upper_arm_yaw_joint` | l_shoulder_roll_link → l_upper_arm_link | Z (yaw) | -1.57 … 1.57 | arm |
| 7 | S07 | `l_elbow_pitch_joint` | l_upper_arm_link → l_forearm_link | Y (pitch) | -2.4 … 0.0 | forearm |
| 8 | S08 | `l_hip_yaw_joint` | base_link → l_hip_yaw_link | Z (yaw) | -0.8 … 0.8 | leg |
| 9 | S09 | `l_hip_roll_joint` | l_hip_yaw_link → l_hip_roll_link | X (roll) | -0.7 … 0.7 | leg |
| 10 | S10 | `l_hip_pitch_joint` | l_hip_roll_link → l_thigh_link | Y (pitch) | -1.57 … 0.8 | leg |
| 11 | S11 | `l_knee_pitch_joint` | l_thigh_link → l_shank_link | Y (pitch) | 0.0 … 2.4 | leg |
| 12 | S12 | `l_ankle_pitch_joint` | l_shank_link → l_ankle_link | Y (pitch) | -0.8 … 0.8 | foot |
| 13 | S13 | `l_ankle_roll_joint` | l_ankle_link → l_foot_link | X (roll) | -0.5 … 0.5 | foot |
| 14 | S14 | `r_shoulder_pitch_joint` | torso_link → r_shoulder_link | Y (pitch) | -2.5 … 2.5 | arm |
| 15 | S15 | `r_shoulder_roll_joint` | r_shoulder_link → r_shoulder_roll_link | X (roll) | -1.57 … 1.57 | arm |
| 16 | S16 | `r_upper_arm_yaw_joint` | r_shoulder_roll_link → r_upper_arm_link | Z (yaw) | -1.57 … 1.57 | arm |
| 17 | S17 | `r_elbow_pitch_joint` | r_upper_arm_link → r_forearm_link | Y (pitch) | -2.4 … 0.0 | forearm |
| 18 | S18 | `r_hip_yaw_joint` | base_link → r_hip_yaw_link | Z (yaw) | -0.8 … 0.8 | leg |
| 19 | S19 | `r_hip_roll_joint` | r_hip_yaw_link → r_hip_roll_link | X (roll) | -0.7 … 0.7 | leg |
| 20 | S20 | `r_hip_pitch_joint` | r_hip_roll_link → r_thigh_link | Y (pitch) | -1.57 … 0.8 | leg |
| 21 | S21 | `r_knee_pitch_joint` | r_thigh_link → r_shank_link | Y (pitch) | 0.0 … 2.4 | leg |
| 22 | S22 | `r_ankle_pitch_joint` | r_shank_link → r_ankle_link | Y (pitch) | -0.8 … 0.8 | foot |
| 23 | S23 | `r_ankle_roll_joint` | r_ankle_link → r_foot_link | X (roll) | -0.5 … 0.5 | foot |
