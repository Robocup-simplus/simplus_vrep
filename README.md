# SimPlus_VRep
This repository is dedicated to the new Rescue simulation environment for Robocupers from Juniors to Majors and is aimed to be a bridge from Robocup Junior Rescue to Robocup Major Rescue competitions, so that a kid could start with it (e.g. by using Scratch to move a simulated robot) and gradually be introduced with more complex problems and languages (e.g. implementing object detection and SLAM in ROS).


- [Overview](#overview)
  - [Structure](#developed-structure)
  - [Demo](#demo)
  - [System Requirements](#system-requirements)
  - [Software Requirements](#software-requirements)
- [Getting Start (Wiki page)](https://github.com/Robocup-simplus/simplus_vrep/wiki)
- [Setup & Run](EASY_SETUP.md)
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

After lots of investigations the team decided to work based on **V-REP** from the three selected platforms: V-REP, Webot, and Gazebo.
V-REP provides a free license for educational purposes and accepts seven programming languages. 

## Developed Structure
The scheme of Simplus V-rep could be found in the figure below.
![Simplus V-rep Structure](docs/img/SimplusVrepStructure.png?raw=true "Simplus V-rep Structure")
The proposed platform structure is consist of 3 main parts; V-REP + models + worlds, Gama Manager + Robot Monitor, & Robot Controlling code.

### V-REP + models + worlds
V-REP released the latest version of V-REP 4.0.0 and named it CoppelliaSim just two weeks ago.
We have tested our developlments also with V-REP 4.0.0 (CoppelliaSim) it works perfectly and even faster.
It was a good sign here that V-REP at its' biggest update is compattible with our developments.
We have prepared bunch of sample models and a sample world.

### Game Manager + Robot Monitor

we have considered two senarios; a server/client senario and a combined version, both senarios include the Game Manager, Robot Monitor, and the Robot Controlling code. The point is that in a server/client based approach the robot controling code (which the teams are soppused to develope) could be separated and run by an different computers which makes it a better solution for compettitions.

#### Game Manager

We have developed a Game Manager that is fed by the rules (whatever it is, finding victim, moving victim or obstacles, moving to a particular position, avoiding traps, to make the list short: robots can even play football:) and we did not limit the rules just to the rescue)

The Game Manager has been developed to
- Control the game state such as Start, Pause, & Stop,
- Calculate the scores based on the fexible rules defined by TC/OCs, (One of the most difficult parts of the TC/OC jobs in Virtual Rescue is fairly calculating the score as it is a simulated environment, so it is necessary to have the automated scoring system)
- Show scoreboard.

#### Robot Monitor
The Robot Monitor shows the robot's sensors status, camera, orientation, & positions along providing a simple robot control panel, and possibility to connect with a real robot which might be intresting for kids.

### Robot Controlling
The Robot Controlling code developed by the teams will be placed here. Simplus V-Rep supports lots of programming languages (e.g. **Scratch**, **Python**, **C**, **C++**, GO, Obejctive C, JAVA, Node.js, ... etc) which makes it available for any age, & any paroblem!

The developing team have prepared 2 sample codes moving one for Scratch, and an other for Python (more samples will be provided if needed).

## Demo
In order to have a better understanding of how the installation and running is performed, we have provided a demo.
Please have a look at the following video:
[https://youtu.be/zule-A18Qzo](https://youtu.be/zule-A18Qzo)

It shows the installation process, and runs a sample of robot controlling code in order to show the robot interaction with the environment.

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
