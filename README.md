# SimPlus_VRep
This repository is dedicated to a Rescue simulation environment for Robocup Juniors and is aimed to be a bridge from Robocup Junior Rescue to Robocup Major Rescue competitions.

![SimPlus on macOS](docs/img/world2.png?raw=true "Simplus on macOS")


- [Install instructions](INSTALL.md)
- [Authors](AUTHORS.md)
- [Changelog](CHANGELOG.md)
- License: [GNU General Public License (GPLv3)](LICENSE.md)

System Requirements
-----------------------

grSim will likely run on a modern dual core PC with a decent graphics card. Typical configuration is:

- Dual Core CPU (2.0 Ghz+)
- 1GB of RAM
- 256MB nVidia or ATI graphics card

Note that it may run on lower end equipment though good performance is not guaranteed.


Software Requirements
---------------------

grSim compiles on Linux (tested on Ubuntu variants only) and Mac OS. It depends on the following libraries:

- [CMake](https://cmake.org/) version 3.5+ 
- [OpenGL](https://www.opengl.org)
- [Qt5 Development Libraries](https://www.qt.io)
- [Open Dynamics Engine (ODE)](http://www.ode.org)
- [VarTypes Library](https://github.com/jpfeltracco/vartypes) forked from [Szi's Vartypes](https://github.com/szi/vartypes)
- [Google Protobuf](https://github.com/google/protobuf)
- [Boost development libraries](http://www.boost.org/) (needed by VarTypes)

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
