# SimPlus_VRep
This repository is dedicated to the new Rescue simulation environment for Robocupers from Juniors to Majors and is aimed to be a bridge from Robocup Junior Rescue to Robocup Major Rescue competitions, so that a kid could start with it (e.g. by using Scratch to move a simulated robot) and gradually be introduced with more complex problems and languages (e.g. implementing object detection and SLAM in ROS).


- [Overview](https://github.com/Robocup-simplus/simplus_vrep/#overview)
  - [Game Manager Features](https://github.com/Robocup-simplus/simplus_vrep/#game-manager-features)
  - [Robot Controlling](https://github.com/Robocup-simplus/simplus_vrep/#robot-controlling)
  - [System Requirements](https://github.com/Robocup-simplus/simplus_vrep/#system-requirements)
  - [Software Requirements](https://github.com/Robocup-simplus/simplus_vrep/#software-requirements)
- [Getting Start](https://github.com/Robocup-simplus/simplus_vrep/wiki)
- [Setup & Run](README.md)
  - [Easy Setup & Run](EASY_SETUP.md)
  - [Manual Setup & Run](MANUAL_SETUP.md)   
    - [Install instructions](MANUAL_SETUP.md#vrep-installation)
    - [Usage](MANUAL_SETUP.md#usage)
- [World and Rules](WORLD.md)
  - [World and Rules](WORLD.md)
  - [Simplus Models](MODELS.md)
- [Authors](AUTHORS.md)
- [Changelog](CHANGELOG.md)

![SimPlus on macOS](docs/img/world2.png?raw=true "Simplus on macOS")

# Overview
This repository is dedicated to the new Rescue simulation environment for Robocupers from Juniors to Majors and is aimed to be a bridge from Robocup Junior Rescue to Robocup Major Rescue competitions, so that a kid could start with it (e.g. by using Scratch to move a simulated robot) and gradually be introduced with more complex problems and languages (e.g. implementing object detection and SLAM by ROS).

A poster entitled as ["A proposal on more advanced Robot Rescue Simulation challenges for Robotics Education"](https://www.researchgate.net/profile/Fatemeh_Pahlevan_Aghababa/publication/336114712_WeROB2019/links/5d8f0692a6fdcc2554a1125f/WeROB2019.pdf) was presented in [Workshop On Educational Robotics-WEROB 2019](https://junior.robocup.org/workshop-on-educational-robotics-werob-2019/). In the poster, the reqiurments of a platform to be used as bridge to filling the gap between RoboCup Junoir Rescue and Virtual Rescue Robot competition for such a development are defined as follows:
- Being free and fully accessible to students to use,
- Ease of installation even on low-spec PCs,
- Interface that is intuitive to use.
- The ability to serve from fundamentals to higher complexity concepts,
- Easy transition to research-based platforms from educational-focused platform

After lots of investigations the team decided to work on V-REP from the three selected platforms: V-REP, Webot, and Gazebo.
V-REP provides a free license for educational purposes and accepts seven programming languages. 

## Developed Structure
The scheme of Simplus V-rep could be found in the figure below.
![Simplus V-rep Structure]("docs/img/SimplusVrepStructure.png"?raw=true "Simplus V-rep Structure")

### Game Manager Features
The Game Manager has been developed to
- Control the game state such as Start, Pause, & Stop,
- Calculate the scores based on the fexible rules defined by TC/OCs, (One of the most difficult parts of the TC/OC jobs in Virtual Rescue is fairly calculating the score as it is a simulated environment, so it is necessary to have the automated scoring system)
- Show scoreboard.

### Robot Controlling
Simplus V-Rep supports lots of programming languages (e.g. Scratch, Python, GO, C, C++, Obejctive C, JAVA, Node.js, ... etc) which makes it available for any age, & any paroblem!


## System Requirements
-----------------------

SimPlus will likely run on a modern dual core PC with a decent graphics card. Typical configuration is:

- Dual Core CPU (2.0 Ghz+)
- 2GB of RAM
- 256MB nVidia or ATI graphics card

Note that it may run on lower end equipment, though good performance is not guaranteed.


## Software Requirements
---------------------

SimPlus compiles and run on Win/Linux/macOS (tested on Ubuntu variants only). It depends on the following libraries:

- [Python](https://www.python.org) version 3.5+ 
- [Vrep Simulation](http://www.coppeliarobotics.com)
- [Google Protobuf](https://github.com/google/protobuf)
- [GRPC](http://grpc.io)
- [Bottle](https://bottlepy.org/docs/dev/) (Only needed for Scratch API)

Simplus Server enviroment 
---------------------
![SimPlus on macOS](docs/img/full.png?raw=true "Simplus server")

Scratch Simplus extention enviroment
---------------------

![Scratch sample code](docs/img/scratch.png?raw=true "Scratch Simplus extention")


