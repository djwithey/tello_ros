import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

# Launch nodes required for joystick operation

def generate_launch_description():
    camera_file = os.path.join(
            get_package_share_directory('tello_driver'),
            'cfg',
            'camera_info.yaml')
    return LaunchDescription([
        Node(package='joy', executable='joy_node', output='screen'),
        Node(package='tello_driver', executable='tello_joy_main', output='screen'),
        Node(package='tello_driver', executable='tello_driver_main', output='screen',
             parameters=[{'camera_info_path': camera_file}],
            ),
    ])
