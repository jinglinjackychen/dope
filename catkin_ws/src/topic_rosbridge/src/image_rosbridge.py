#!/usr/bin/env python3

from arg_robotics_tools import websocket_rosbridge as socket
from sensor_msgs.msg import CompressedImage
import rospy
import base64

class color_image_repub():
    def __init__(self):
        self.easy_socket = socket.ros_socket('192.168.50.10', 9090)
        self.easy_socket.subscriber('/camera_right/color/image_raw/compressed', self.sub_callback, 1)
        self.image_pub = rospy.Publisher('/camera_right/color/image_raw/compressed', CompressedImage, queue_size = 1)
        self.compressed_image = CompressedImage()

    def sub_callback(self, msg):
        self.compressed_image.header.seq = msg['header']['seq']
        self.compressed_image.header.stamp.secs = msg['header']['stamp']['secs']
        self.compressed_image.header.stamp.nsecs = msg['header']['stamp']['nsecs']
        self.compressed_image.header.frame_id = msg['header']['frame_id']
        self.compressed_image.format = msg['format']
        base64_bytes = msg['data'].encode('ascii')
        image_bytes = base64.b64decode(base64_bytes)
        self.compressed_image.data = image_bytes
        self.image_pub.publish(self.compressed_image)

class depth_image_repub():
    def __init__(self):
        self.easy_socket = socket.ros_socket('192.168.50.10', 9090)
        self.easy_socket.subscriber('/camera_right/aligned_depth_to_color/image_raw/compressedDepth', self.sub_callback, 1)
        self.image_pub = rospy.Publisher('/camera_right/aligned_depth_to_color/image_raw/compressedDepth', CompressedImage, queue_size = 1)
        self.compressed_image = CompressedImage()
        self.key = bytes([0x00, 0x00, 0x00, 0x00, 0x20, 0x92, 0x34, 0x02, 0xA8, 0x7F, 0x00, 0x00])
        # [0, 0, 0, 0, 32, 146, 52, 2, 168, 127, 0, 0]

    def sub_callback(self, msg):
        self.compressed_image.header.seq = msg['header']['seq']
        self.compressed_image.header.stamp.secs = msg['header']['stamp']['secs']
        self.compressed_image.header.stamp.nsecs = msg['header']['stamp']['nsecs']
        self.compressed_image.header.frame_id = msg['header']['frame_id']
        self.compressed_image.format = msg['format']
        base64_bytes = msg['data'].encode('ascii')
        image_bytes = base64.b64decode(base64_bytes)
        self.compressed_image.data = self.key + image_bytes
        self.image_pub.publish(self.compressed_image)

class pose_repub():
    def __init__(self):
        self.easy_socket = socket.ros_socket('192.168.50.43', 9090)
        self.talker = self.easy_socket.publisher('/dope/pose_sugar', 'geometry_msgs/PoseStamped')
        self.pose_sub = rospy.Subscriber('/dope/pose_sugar', PoseStamped, self.sub_callback)
        self.data = {'header':{'seq':0, 'stamp':{'secs':0, 'nsecs':0},'frame_id':''}, 'pose':{'position':{'x':0.0, 'y':0.0, 'z':0.0}, 'orientation':{'x':0.0, 'y':0.0, 'z':0.0, 'w':0.0}}}

    def sub_callback(self, msg):
        self.data['header']['seq'] = msg.header.seq
        self.data['header']['stamp']['secs'] = msg.header.stamp.secs
        self.data['header']['stamp']['nsecs'] = msg.header.stamp.nsecs
        self.data['header']['frame_id'] = msg.header.frame_id
        self.data['pose']['position']['x'] = msg.pose.position.x
        self.data['pose']['position']['y'] = msg.pose.position.y
        self.data['pose']['position']['z'] = msg.pose.position.z
        self.data['pose']['orientation']['x'] = msg.pose.orientation.x
        self.data['pose']['orientation']['y'] = msg.pose.orientation.y
        self.data['pose']['orientation']['z'] = msg.pose.orientation.z
        self.data['pose']['orientation']['w'] = msg.pose.orientation.w
        self.easy_socket.pub(self.talker, self.data)

if __name__=='__main__':
    rospy.init_node("psub_image", anonymous=False)

    color = color_image_repub()
    depth = depth_image_repub()
    pose = pose_repub()
    
    rospy.spin()