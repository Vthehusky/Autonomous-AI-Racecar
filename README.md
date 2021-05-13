# Autonomous-AI-Racecar

## Chassis and car ##

The final result, when completed will look similar to the image of the racecar included below. I have changed the basic build and replaced some of the physical components and accessories based on my custom build.

![Image of AI Racecar](https://github.com/Vthehusky/Autonomous-AI-Racecar/blob/main/Images/1.jpeg)

## Modified chassis build (Progres so far...) ##

You can check out more build images and chassis subsystem test videos in the Images folder

![Image of my AI Racecar](https://github.com/Vthehusky/Autonomous-AI-Racecar/blob/main/Images/77.jpeg)

## Firmware development (Progres so far...) ##

The implementation of the basic drive features of steering control and mobility based on perception have been taken care of, via the scipts in jetracer and notebooks directories.
However, the firmware is not based on a middleware like ROS.

Hence, I am currently working to encapsulate the entire functionality in ROS. The original Tamiya based build also did not use any localization techniques. This will be a new update to my custom build. I will most likely use dead reckoning combined with landmark detection and tracking to implement localization on offline maps. I do not have a LiDAR sensor at the moment, but I will implement Adaptive Monte Carlo Localization (AMCL), as soon as I buy one since I have already implemented a localization mechanism based off AMCL in ROS (https://bitbucket.org/vinaypra/vinaypra_navfivedays/src/master/).

### Check out my work in ROS at: https://bitbucket.org/vinaypra/ ###

I will try to improve localization further with some of the indoor localization techniques I have been developing as a part of another project. Under Dr. Lan Zhang, I have been working on the project Intelligent Wireless Sensing - Novel applications of machine learning algorithms for IEEE 802.11 for wireless sensing.
My role in the team:
♦ Setting up the required hardware test benches using Jetson Nano and laptops running custom builds of CSI tools acting as wireless nodes, to collect Channel State Information (CSI).
♦ Pre-processing and filtering the CSI data for multi-domain (time, frequency, wavelet and deep features) for feature extraction.
♦ Applying machine learning and model-based algorithms for state estimation in sensing applications.

### Check out the details at: https://events.mtu.edu/event/augmenting_radio_environments_for_better_wireless_ecosystems ###
