The objective of this package is to make the car move through GPS readings to a defined location, or WayPoint.

To make development objectives simpler, it has been broken down into the following steps:

1) Creating a GPS Subscriber: We subscribe to the **/fix** topic. Then, extract the latitude and longitude. 
2) We make a function that calculates the distance from the current position to a given waypoint. This distance has to be determined through an algorithm for Earth distance calculations. For instance, through the Vincency method. https://en.wikipedia.org/wiki/Vincenty%27s_formulae
3) We create a Class that publishes in the appropriate topic to move the car. In this case, move without any security system, which is publishing in the **/catvehicle/cmd_vel_safe.**
4) Next, we create an Action Server that, given a waypoint, returns the distance to that waypoint until the target is reached. Because the distance is calculated in meters, it will be enough with integer values.
5) Finally, we create an Action Client that calls this server and moves the car to the given waypoint. We have implemented an algorithm that, as distances change, can change the car's direction to get as close as possible.