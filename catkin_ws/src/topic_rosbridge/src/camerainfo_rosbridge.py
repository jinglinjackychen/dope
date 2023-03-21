#!/usr/bin/env python3

from arg_robotics_tools import websocket_rosbridge as socket
from sensor_msgs.msg import CompressedImage,CameraInfo
from geometry_msgs.msg import PoseStamped
import rospy
import base64

class camera_info_repub():
    def __init__(self):
        self.easy_socket = socket.ros_socket('192.168.50.10', 9090)
        self.easy_socket.subscriber('/camera_right/color/camera_info', self.sub_callback, 1)
        self.camera_info_pub = rospy.Publisher('/camera_right/color/camera_info', CameraInfo, queue_size = 1)
        self.camera_info = CameraInfo()

    def sub_callback(self, msg):
        self.camera_info.header.seq = msg['header']['seq']
        self.camera_info.header.stamp.secs = msg['header']['stamp']['secs']
        self.camera_info.header.stamp.nsecs = msg['header']['stamp']['nsecs']
        self.camera_info.header.frame_id = msg['header']['frame_id']
        self.camera_info.height = msg['height']
        self.camera_info.width = msg['width']
        self.camera_info.distortion_model = msg['distortion_model']
        self.camera_info.D = msg['D']
        self.camera_info.K = msg['K']
        self.camera_info.R = msg['R']
        self.camera_info.P = msg['P']
        self.camera_info.binning_x = msg['binning_x']
        self.camera_info.binning_y = msg['binning_y']
        self.camera_info.roi.x_offset = msg['roi']['x_offset']
        self.camera_info.roi.y_offset = msg['roi']['y_offset']
        self.camera_info.roi.height = msg['roi']['height']
        self.camera_info.roi.width = msg['roi']['width']
        self.camera_info.roi.do_rectify = msg['roi']['do_rectify']
        self.camera_info_pub.publish(self.camera_info)

if __name__=='__main__':
    rospy.init_node("psub_image", anonymous=False)

    camera_info = camera_info_repub()
    
    rospy.spin()