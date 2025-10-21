import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.callback,
            10
        )
    
    def callback(self, msg):
        self.get_logger().info('i heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    
    node = ListenerNode()
    
    rclpy.spin(node)
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()