#!/usr/bin/env python

# This node will read from the /catvehicle/cmd_vel topic and publish into the /catvehicle/cmd_vel_safe topic. 
# /catvehicle/cmd_vel_safe is the topic where our cmdvel2gazebo.py script reads the Twist data.

# We will read from the /distanceEstimator/angle and /distanceEstimator/dist topics.

# Based on the readings of the /distanceEstimator/ topics, this node will filter the Twist messages received in the /catvehicle/cmd_vel topic.

# If the distance is lower than a value, the Twist that we publish in the /catvehicle/cmd_vel_safe topic will be a STOP message (we set the velocity values to 0).

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class ObstacleStopper(object):
    def __init__(self, minimum_distance=0.0):
        self._minimum_distance = minimum_distance
        rospy.Subscriber("/catvehicle/cmd_vel", Twist, self.cmdvel_callback)
        self.pub_cmdvel_safe = rospy.Publisher('/catvehicle/cmd_vel_safe', Twist, queue_size=0)
        
    def cmdvel_callback(self,data):
        try:
            closest_distance = rospy.wait_for_message('/distanceEstimator/dist', Float32, timeout=1).data
        except:
            rospy.logwarn("Time out /distanceEstimator/dist")
            closest_distance = None
        
        safe_twist = data
        if closest_distance:
            
            object_detected = closest_distance < self._minimum_distance
            if object_detected:
                safe_twist.linear.x = 0.0
            else:
                pass

        else:
            safe_twist.linear.x = 0.0 
        
        self.pub_cmdvel_safe.publish(safe_twist)
        
    
    
    def listener(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('obstacle_stopper_node', anonymous=True)
    os = ObstacleStopper(minimum_distance= 5.0)
    os.listener()
