# Joint Map

Joint origins are in the PARENT link frame at zero pose (metres).

## Hierarchy

```
base_link
    └─ torso_link  <- waist_yaw_joint [revolute, axis 0 0 1]
        └─ neck_link  <- neck_yaw_joint [revolute, axis 0 0 1]
            └─ head_link  <- head_pitch_joint [revolute, axis 0 1 0]
        └─ l_shoulder_link  <- l_shoulder_pitch_joint [revolute, axis 0 1 0]
            └─ l_shoulder_roll_link  <- l_shoulder_roll_joint [revolute, axis 1 0 0]
                └─ l_upper_arm_link  <- l_upper_arm_yaw_joint [revolute, axis 0 0 1]
                    └─ l_forearm_link  <- l_elbow_pitch_joint [revolute, axis 0 1 0]
                        └─ l_hand_link  <- l_wrist_fixed_joint [fixed]
        └─ r_shoulder_link  <- r_shoulder_pitch_joint [revolute, axis 0 1 0]
            └─ r_shoulder_roll_link  <- r_shoulder_roll_joint [revolute, axis 1 0 0]
                └─ r_upper_arm_link  <- r_upper_arm_yaw_joint [revolute, axis 0 0 1]
                    └─ r_forearm_link  <- r_elbow_pitch_joint [revolute, axis 0 1 0]
                        └─ r_hand_link  <- r_wrist_fixed_joint [fixed]
    └─ l_hip_yaw_link  <- l_hip_yaw_joint [revolute, axis 0 0 1]
        └─ l_hip_roll_link  <- l_hip_roll_joint [revolute, axis 1 0 0]
            └─ l_thigh_link  <- l_hip_pitch_joint [revolute, axis 0 1 0]
                └─ l_shank_link  <- l_knee_pitch_joint [revolute, axis 0 1 0]
                    └─ l_ankle_link  <- l_ankle_pitch_joint [revolute, axis 0 1 0]
                        └─ l_foot_link  <- l_ankle_roll_joint [revolute, axis 1 0 0]
    └─ r_hip_yaw_link  <- r_hip_yaw_joint [revolute, axis 0 0 1]
        └─ r_hip_roll_link  <- r_hip_roll_joint [revolute, axis 1 0 0]
            └─ r_thigh_link  <- r_hip_pitch_joint [revolute, axis 0 1 0]
                └─ r_shank_link  <- r_knee_pitch_joint [revolute, axis 0 1 0]
                    └─ r_ankle_link  <- r_ankle_pitch_joint [revolute, axis 0 1 0]
                        └─ r_foot_link  <- r_ankle_roll_joint [revolute, axis 1 0 0]
```

## Joint origins

| Joint | Type | Parent | xyz (m) |
|---|---|---|---|
| `waist_yaw_joint` | revolute | base_link | 0 0 0.04 |
| `neck_yaw_joint` | revolute | torso_link | 0 0 0.25 |
| `head_pitch_joint` | revolute | neck_link | 0 0 0.04 |
| `l_shoulder_pitch_joint` | revolute | torso_link | 0 0.14 0.21 |
| `l_shoulder_roll_joint` | revolute | l_shoulder_link | 0 0 0 |
| `l_upper_arm_yaw_joint` | revolute | l_shoulder_roll_link | 0 0 -0.03 |
| `l_elbow_pitch_joint` | revolute | l_upper_arm_link | 0 0 -0.12 |
| `l_wrist_fixed_joint` | fixed | l_forearm_link | 0 0 -0.11 |
| `l_hip_yaw_joint` | revolute | base_link | 0 0.07 -0.04 |
| `l_hip_roll_joint` | revolute | l_hip_yaw_link | 0 0 -0.03 |
| `l_hip_pitch_joint` | revolute | l_hip_roll_link | 0 0 -0.02 |
| `l_knee_pitch_joint` | revolute | l_thigh_link | 0 0 -0.2 |
| `l_ankle_pitch_joint` | revolute | l_shank_link | 0 0 -0.2 |
| `l_ankle_roll_joint` | revolute | l_ankle_link | 0 0 -0.02 |
| `r_shoulder_pitch_joint` | revolute | torso_link | 0 -0.14 0.21 |
| `r_shoulder_roll_joint` | revolute | r_shoulder_link | 0 0 0 |
| `r_upper_arm_yaw_joint` | revolute | r_shoulder_roll_link | 0 0 -0.03 |
| `r_elbow_pitch_joint` | revolute | r_upper_arm_link | 0 0 -0.12 |
| `r_wrist_fixed_joint` | fixed | r_forearm_link | 0 0 -0.11 |
| `r_hip_yaw_joint` | revolute | base_link | 0 -0.07 -0.04 |
| `r_hip_roll_joint` | revolute | r_hip_yaw_link | 0 0 -0.03 |
| `r_hip_pitch_joint` | revolute | r_hip_roll_link | 0 0 -0.02 |
| `r_knee_pitch_joint` | revolute | r_thigh_link | 0 0 -0.2 |
| `r_ankle_pitch_joint` | revolute | r_shank_link | 0 0 -0.2 |
| `r_ankle_roll_joint` | revolute | r_ankle_link | 0 0 -0.02 |
