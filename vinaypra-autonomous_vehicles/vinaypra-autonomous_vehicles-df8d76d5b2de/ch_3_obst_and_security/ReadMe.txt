The most important element in autonomous vehicles is security.
To have a safer car, we need, at minimum, two elements:

**Obstacle Detection**
**System Failure Measures**

For security reasons, the car shouldn't be moved directly through a typical /cmd_vel topic.

It needs two barriers:

**DeadMansSwitch**: When control communication is lost, autonomous vehicles have to move to a safe state. For our implementation, the car will be made to stop in case the movement commands aren't published at a rate higher than 5Hz.
**ObstacleDetection**: When an obstacle is detected, the vehicle must stop until the obstacle is removed. For our implementation, obstacles are detected.