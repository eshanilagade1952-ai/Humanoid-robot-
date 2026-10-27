# 08 — Future Simulation Recommendations
1. **Reconcile with CAD first** (M1–M3); regenerate; re-run `validate.py`. Do nothing else before this.
2. **Meshes:** export per-link STL/DAE in link frame; keep high-poly for visual, ≤ ~500 faces convex hulls for collision.
3. **Move to xacro** with macros for `arm(side)` and `leg(side)` once dimensions are real — cuts duplication.
4. **Verify** with `check_urdf`, `urdf_to_graphiz`, RViz + `joint_state_publisher_gui` (sweep every joint, confirm direction).
5. **Isaac Sim:** URDF importer → PhysX articulation; fix base or use a stand for first tests; then tune drives (stiffness/damping) from servo specs.
6. **Unreal:** treat as visualization — import meshes via FBX/USD; drive from joint-state stream rather than Unreal physics.
7. **Add:** self-collision exclusion pairs, IMU link at torso, foot contact sensors/frames, actuator velocity/effort from datasheets.
8. **Control later:** ros2_control hardware interface keyed to the logical servo table in `03_dof_map.md`.
