#! /usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix
#https://pypi.python.org/pypi/geopy
from geopy.distance import vincenty
from geometry_msgs.msg import Vector3

class WayPoint():
    def __init__(self, latitude, longitude, altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        
    def print_data(self):
        return "["+str(self.latitude)+","+str(self.longitude)+","+str(self.altitude)+"]


class GpsClass(object):
    def __init__(self):
        self._sub = rospy.Subscriber('/fix', NavSatFix, self.callback)
        self.latitude = 0.0
        self.longitude = 0.0
        self.altitude = 0.0
        self.testwaypoint = WayPoint(49.900090,8.899960,0.000000)

     def callback(self,msg):
        self.latitude, self.longitude, self.altitude = self.remove_noise(msg.latitude, msg.longitude, msg.altitude)
        #rospy.loginfo('Origin [latitude,longitude,altitude]=[%f,%f,%f]', self.latitude, self.longitude, self.altitude)
        #rospy.loginfo('Waypoint [latitude,longitude,altitude]=[%f,%f,%f]', self.testwaypoint.latitude, self.testwaypoint.longitude, self.testwaypoint.altitude)
        #rospy.loginfo('Distance to WayPointTest=%f', self.distance_from_waypoint(self.testwaypoint))
    
    def remove_noise(self,latitude,longitude,altitude):
        return round(latitude,5),round(longitude,5),round(altitude,1)

    def get_current_gps_pos(self):
        # Returns newest GPS current position in a Waypoint Format
        return WayPoint(self.latitude, self.longitude, self.altitude)
    
    def get_direction_to_waypoint(self, waypoint):
        direction = Vector3()
        direction.x = waypoint.latitude - self.latitude
        direction.y = waypoint.longitude - self.longitude
        direction.z = waypoint.altitude - self.altitude

    def distance_from_waypoint(self,waypoint):
        # Calculates the distance (in meters) from specified waypoint using Vincenty method
        # We are concerned with latitude and longitude only, here
        origin = (self.latitude, self.longitude)
        waypoint = (waypoint.latitude, waypoint.longitude)
        return vincenty(origin, waypoint).meters
    

if __name__ == '__main__':
  rospy.init_node('gps_topic_subscriber')
  GpsClass()
  rospy.spin()