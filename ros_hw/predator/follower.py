#!/usr/bin/env python2

import rospy
import time
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import sqrt, atan2, pi, log1p

class Follower:
	def __init__(self):
		self.pose = Pose()

		self.sub1 = rospy.Subscriber('/turtle1/pose', Pose, self.follow_turtle)
		self.sub2 = rospy.Subscriber('/leo/pose', Pose, self.get_self_pos)
		self.pub = rospy.Publisher('/leo/cmd_vel', Twist, queue_size=10)

	def get_self_pos(self, current_pose):
		self.pose = current_pose
	
	def follow_turtle(self, target_pose):
		distance = sqrt((target_pose.x - self.pose.x)**2 + (target_pose.y - self.pose.y)**2)
		angle = atan2(target_pose.y - self.pose.y, target_pose.x - self.pose.x) - self.pose.theta

		while angle > pi:
			angle -= 2 * pi
		while angle < -pi:
			angle += 2 * pi

		if distance > 1e-2:
			msg = Twist()
			msg.linear.x = 1.5 * distance
			msg.angular.z = (10 / log1p(distance + 1e-8)) * angle
			self.pub.publish(msg)

