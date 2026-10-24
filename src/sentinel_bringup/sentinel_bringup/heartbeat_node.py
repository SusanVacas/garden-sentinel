#!/usr/bin/env python3
"""
Garden Sentinel — heartbeat_node
Publishes a status string every 2 seconds.
Phase 1: confirms ROS2 stack is alive on the Pi :3.
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HeartbeatNode(Node):
    def __init__(self):
        super().__init__('heartbeat_node')
        self.publisher_ = self.create_publisher(
            String, '/sentinel/status', 10)
        self.timer = self.create_timer(
            2.0, self.publish_status)
        self.get_logger().info(
            'Garden Sentinel heartbeat node started.')

    def publish_status(self):
        msg = String()
        msg.data = 'Garden Sentinel online'
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Published: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = HeartbeatNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
