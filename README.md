# SimPlus_VRep
This repository is dedicated to a Rescue simulation environment for Robocup Juniors and is aimed to be a bridge from Robocup Junior Rescue to Robocup Major Rescue competitions.

![SimPlus on macOS](docs/img/world2.png?raw=true "Simplus on macOS")

- [Getting Start](https://github.com/Robocup-simplus/simplus_vrep/wiki)
- [Setup](README.md)
  - [Easy Setup and Run(only Mac)](EASY_SETUP.md)
  - [Manual Setup](MANUAL_SETUP.md)   
    - [Install instructions](MANUAL_SETUP.md#vrep-installation)
    - [Usage](MANUAL_SETUP.md#usage)
- [Simplus Models](MODELS.md)
- [Authors](AUTHORS.md)
- [Changelog](CHANGELOG.md)

System Requirements
-----------------------

SimPlus will likely run on a modern dual core PC with a decent graphics card. Typical configuration is:

- Dual Core CPU (2.0 Ghz+)
- 2GB of RAM
- 256MB nVidia or ATI graphics card

Note that it may run on lower end equipment, though good performance is not guaranteed.


Software Requirements
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


