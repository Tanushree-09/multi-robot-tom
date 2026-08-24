import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32


class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')

        self.declare_parameter('robot_name', 'robot_A')
        self.robot_name = self.get_parameter('robot_name').value

        self.cmd_pub = self.create_publisher(
            Twist,
            f'/{self.robot_name}/cmd_vel',
            10
        )

        self.sensor_pub = self.create_publisher(
            Float32,
            f'/{self.robot_name}/front_distance',
            10
        )

        self.timer = self.create_timer(0.1, self.control_loop)

        self.distance = 5.0

        self.get_logger().info(
            f'Robot controller started for {self.robot_name}'
        )

    def control_loop(self):

        # Temporary perception value.
        # The real Webots sensor will be connected next.
        distance = self.distance

        sensor_msg = Float32()
        sensor_msg.data = float(distance)
        self.sensor_pub.publish(sensor_msg)

        cmd = Twist()

        if distance > 0.8:
            cmd.linear.x = 0.5
        else:
            cmd.linear.x = 0.0
            cmd.angular.z = 0.8

        self.cmd_pub.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = RobotController()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()