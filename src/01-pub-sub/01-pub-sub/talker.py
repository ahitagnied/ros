import rclpy
from rclpy.node import Node

from std_msgs.msg import String


T = 0.5


class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, 'topic', 10) # topic, messgae type string, queue size 10
        self.timer_ = self.create_timer(T, self.timer_callback) # call timer callback every T seconds
        self.count = 0
    
    def timer_callback(self):
        msg = String()
        msg.data = 'hello, ros2! %d' % self.count
        self.count += 1
        self.get_logger().info('publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    # make node

    # use node 

    # destroy node


if __name__ == '__main__':
    main()