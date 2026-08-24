import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class WebotsRobotDriver(Node):

    def __init__(self):
        super().__init__('webots_robot_driver')

        self.declare_parameter('robot_name', 'robot_A')
        self.robot_name = self.get_parameter('robot_name').value

        self.cmd_sub = self.create_subscription(
            Twist,
            f'/{self.robot_name}/cmd_vel',
            self.cmd_vel_callback,
            10
        )

        self.get_logger().info(
            f'Webots ROS 2 driver interface ready for {self.robot_name}'
        )

    def cmd_vel_callback(self, msg):
        self.get_logger().info(
            f'{self.robot_name}: '
            f'linear={msg.linear.x:.2f}, '
            f'angular={msg.angular.z:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = WebotsRobotDriver()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()