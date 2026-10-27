# HANDOVER (updated for Task 2)
## What exists
- Task 1: placeholder URDF (23 DOF), docs, validator. See HANDOVER_TASK1.md and REVIEW_PACKET_TASK1.md.
- Task 2: ROS 2 Humble proof (check_urdf, robot_state_publisher, RViz, joint states, TF tree) and a Gazebo import. See REVIEW_PACKET.md.

## How to run (Windows 11 + WSL2 Ubuntu 22.04 + ROS 2 Humble)
RViz: cd ~/bhiv_humanoid_digital_twin && LIBGL_ALWAYS_SOFTWARE=1 ros2 launch launch/display.launch.py
  In RViz: Fixed Frame = base_link, Add > RobotModel, Description Topic = /robot_description.
Gazebo tab 1: LIBGL_ALWAYS_SOFTWARE=1 ros2 launch ros_gz_sim gz_sim.launch.py gz_args:="-r --render-engine ogre empty.sdf"
Gazebo tab 2: ros2 run ros_gz_sim create -file urdf/bhiv_humanoid_foundation.urdf -name bhiv_humanoid -z 0.6
Do not run RViz and Gazebo together on a low-memory laptop. Stop with Ctrl+C.

## Next steps
1. Get the real CAD and final hardware revision (blocker).
2. Fill real values into docs/reconciliation_matrix.md; mark rows CONFIRMED / NEEDS CORRECTION.
3. Update dimensions in tools/generate.py, regenerate, run tools/validate.py.
4. Export per-link STL meshes (visual + collision) and reference them in the URDF.
5. Check every joint direction and limit against the physical servos.
6. Only then move to controllers and motion testing (next task).

## Do not
Invent dimensions, mark items CONFIRMED without evidence, or move to hardware control.
