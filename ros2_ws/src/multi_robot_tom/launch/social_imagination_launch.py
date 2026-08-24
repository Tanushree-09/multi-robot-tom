from launch import LaunchDescription
from launch_ros.actions import Node
from webots_ros2_driver.webots_launcher import WebotsLauncher
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    package_dir = get_package_share_directory('multi_robot_tom')
    world = os.path.join(package_dir, 'worlds', 'social_imagination.wbt')

    webots = WebotsLauncher(
        world=world,
        ros2_supervisor=True,
    )

    robot_a = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={
            'WEBOTS_ROBOT_NAME': 'robot_A',
        },
    )

    robot_b = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={
            'WEBOTS_ROBOT_NAME': 'robot_B',
        },
    )

    robot_c = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={
            'WEBOTS_ROBOT_NAME': 'robot_C',
        },
    )

    return LaunchDescription([
        webots,
        robot_a,
        robot_b,
        robot_c,
    ])
