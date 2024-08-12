# Autonomous-AI-Racecar

## Update: ##
Repository restructuring: It has been a little while since I last worked on this project. There are a lot of changes planned to be rolled out over the next 2 weeks.
The main changes coming up are as follows:
- Setting up a proper catkin_ws for the ROS and ROS 2 builds.
- Set up the necessary submodules in the src director to cleanly partition various parts of the SW stack (navigation, planners, control and ROS-CAN interface layer, among other parts).
- Implement Git workflows for managing releases and ensuring smooth continuous integration and deployment.
- Set up GitHub Actions for automated testing, building, and deployment of the software.

## Hardware build ##
This has now been moved to the hardware_build directory README file. Please refer to that directory for the hardware build related progress.

## Firmware development ##

The implementation of the basic drive features of steering control and mobility based on perception have been taken care of, via the scipts in jetracer and notebooks directories.

Hence, I am currently working to encapsulate the entire functionality in ROS. The original Tamiya based build also did not use any localization techniques. This will be a new update to my custom build. I will most likely use dead reckoning combined with landmark detection and tracking to implement localization on offline maps. I do not have a LiDAR sensor at the moment, but the idea is to implement Adaptive Monte Carlo Localization (AMCL) since I have already implemented a localization mechanism based off AMCL in ROS (https://bitbucket.org/vinaypra/vinaypra_navfivedays/src/master/).

## Update: Firmware development - Added CAN to ROS based framework ##

The actual codebase has been imported from another personal repository on BitBucked. The implementation is maintained at -
https://bitbucket.org/vinaypra/autonomous_vehicles/src/master/

### Check out my work in ROS at: https://bitbucket.org/vinaypra/ ###

### Planned Enhancements ###
- Migration to Jetson Orin: Planning to enhance the JetRacer platform for improved AI processing and autonomous racing capabilities.

- Implementation of CAN Bus Motor Control: Developing a custom SocketCAN-ROS interface for motor control via CAN bus using a PIC18F microcontroller.

- Integration of Advanced Stereo Vision: Incorporating an OAK D-Lite stereo vision camera alongside the Raspberry Pi Camera v2 for advanced perception.

- Development of Motion Planning Algorithms: Creating motion planning algorithms (Hybrid A* and TEB) utilizing dual-camera inputs for autonomous navigation.

- Enhancing Obstacle Detection: Implementing real-time obstacle and object detection using DepthAI's Object Tracker with KCF, Kalman filter, and Hungarian algorithm.

