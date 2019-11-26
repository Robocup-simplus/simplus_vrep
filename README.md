# SimPlus_VRep
This repository is dedicated to a Rescue simulation environment for Robocup Juniors and is aimed to be a bridge from Robocup Junior Rescue to Robocup Major Rescue competitions.

![SimPlus on macOS](docs/img/world2.png?raw=true "Simplus on macOS")

- [Getting Start](https://github.com/Robocup-simplus/simplus_vrep/wiki)
- [Install instructions](INSTALL.md)
- [Simplus Models](Models.md)
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
- [Vrep Simulation](https://www.coppeliarobotics.com)
- [Google Protobuf](https://github.com/google/protobuf)
- [GRPC](http://grpc.io)
- [Bottle](https://bottlepy.org/docs/dev/) (Only needed for Scratch API)


Please consult the [install instructions](INSTALL.md) for more details.


# Usage
1.  Run the VREP and Start the world (click on play icon)
2. Run Clients:
```bash
python client.py
```
3. Run Servers for each client:
```bash
python server.py
```
4. Manage and Watch the Game form Lua Panel 

![SimPlus on macOS](docs/img/full.png?raw=true "Simplus on macOS")

