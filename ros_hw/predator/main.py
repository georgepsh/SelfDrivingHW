#!/usr/bin/env python2

import rospy
from position_messager import Messager
from follower import Follower

rospy.init_node('predator_test')

# T = Messager()
F = Follower()
rospy.spin()
