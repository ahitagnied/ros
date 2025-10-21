import rclpy
from rclpy.node import Node

from std_msgs.msg import String


T = 0.5


class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(T, self.callback)
    
    def callback(self):
        msg = String()
        msg.data = 'hello ros2!'
        self.publisher.publish(msg)
        self.get_logger().info('publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node = TalkerNode()
    
    rclpy.spin(node)
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()