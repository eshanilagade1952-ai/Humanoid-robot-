import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    here = os.path.dirname(os.path.realpath(__file__))
    urdf = os.path.normpath(os.path.join(here, '..', 'urdf', 'bhiv_humanoid_foundation.urdf'))
    with open(urdf) as f:
        robot_description = f.read()
    return LaunchDescription([
        Node(package='robot_state_publisher', executable='robot_state_publisher',
             parameters=[{'robot_description': robot_description}]),
        Node(package='joint_state_publisher_gui', executable='joint_state_publisher_gui'),
        Node(package='rviz2', executable='rviz2', arguments=['-d', os.path.normpath(os.path.join(here, '..', 'rviz', 'bhiv.rviz'))]),
    ])
