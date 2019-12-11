The installation is based on 2 approaches; 
- in the first approach the Game Manager & the Robot Controlling Code are placed in the same file which could be useful for training)
- in the second approach the Game Manager & the Robot Controlling Code are placed in different files by a Client/Server senario and the connection is based on ports which makes it suitable for competition).

> It should be noted that the for now using the Scratch is just available through the second approach.  

> Since the approach2 uses ports to communicate, and several ports might be left open by the previously ran programs, it is advised to run the `clear.sh`, `clear.bat`, & `clear.sh` with respect to your OS before each run.

Follow the setup instruction based on your OS:
- [macOS](#macOS)
  - [macOS Installation](https://github.com/Robocup-simplus/simplus_vrep/blob/master/EASY_SETUP.md#installation)
  - [World setup](https://github.com/Robocup-simplus/simplus_vrep/blob/master/EASY_SETUP.md#world-setup)
  - [Run](https://github.com/Robocup-simplus/simplus_vrep/blob/master/EASY_SETUP.md#run)
- [Windows](#Windows)
  - [Windows Installation](https://github.com/Robocup-simplus/simplus_vrep/blob/master/EASY_SETUP.md#installation-1)
  - [World setup](#world-setup-1)
  - [Run](#run-1)
- [Ubuntu 16.04](#ubuntu-1604)
  - [Installation](#installation-2)
  - [World setup](#world-setup-2)
  - [Run](#run-2)
- [Ubuntu 16.04](#ubuntu-1804)
  - [Installation](#installation-3)
  - [World setup](#world-setup-3)
  - [Run](#run-3)
- [Setup for Scratch](#setup-for-scratch)  

---

# macOS  
In order to make the communication with server easier, some applications and scripts are created. You can choose using applications or scripts .The Applications will be run by duoble clicking on them and you can find the current running application list on the mac's top menu.
  
  ![Applications status](docs/img/mac_runpackage.png?raw=true "Applications status")

You can close this applications using 'close' icon near them. It should be mentioned that the 0% sign below the application name means that it is running. The application name will be automatically removed from the menu whenever it's job is finished.

## Installation

### Using  [installer Application](https://github.com/Robocup-simplus/simplus_vrep/raw/master/easy_setup/mac/installer.zip) 
```bash
 Double click on the "installer" application and the server will be installed on the Desktop directory
(You will recieve a dialog pop up at the end of the installation process).
```
- In case you face any error use [installer_full Application](https://github.com/Robocup-simplus/simplus_vrep/raw/master/easy_setup/mac/installer_full.zip) and Double click on it.



### Using [installer Script](https://raw.githubusercontent.com/Robocup-simplus/simplus_vrep/master/easy_setup/mac/installer.sh)
```bash
1. Put the file where ever you want the simplus package be installed in.
2. Open the terminal and write "sh ", drag and drop the "installer.sh" file to terminal then press enter
```
- The installation path should not include any " ", if there were any, the simplus vrep will be installed in the path shown at the end of the installation (you can easily cut the  "simplus_vrep" folder and place it whereever you want after the installation is finished).
- In case you face any error use [installer_full.sh](https://raw.githubusercontent.com/Robocup-simplus/simplus_vrep/master/easy_setup/mac/installer_full.sh) and repeat step 3.

## World setup

### Using Application
```bash
Double click on the "simulator" application
(It can be found in "simplus_vrep/easy_setup/mac" directory)
```

### Using Script
```bash
Open the terminal and write "sh ", drag and drop the "simulator.sh" file to terminal then press enter
(It can be found in "simplus_vrep/easy_setup/mac" directory)
``` 

## Run 
There is two methods to communicate with the robot:
Approach1: is based on V-rep python API (there is no client and server),
Approach2: is based on remote API (the teams should use client to control robot and the server is responnsible for other things prepared by technical committee) 

> Remember to Stop the V-REP Simulator (by the V-REP Stop bottom) & Play agein (by the V-REP Start bottom) before starting a new Run.

### Approach1
#### Using Application
```bash
Double click on the "run1" application
(It can be found in "simplus_vrep/easy_setup/mac" directory)
```

#### Using Script

```bash
Open the terminal and write "sh ", drag and drop the "run1.sh" file to terminal then press enter
(It can be found in "simplus_vrep/easy_setup/mac" directory)
```

### Approach 2
#### Using Application
```bash
1. Double click on the "run2_client" application
2. Double click on the "run2_server" application
(They can be found in "simplus_vrep/easy_setup/mac" directory)

```

#### Using Script
```bash
1. Open the terminal and write "sh ", drag and drop the "run2_client.sh" file to terminal then press enter
2. Open the terminal and write "sh ", drag and drop the "run2_server.sh" file to terminal then press enter
(They can be found in `simplus_vrep/easy_setup/mac` directory)

```

---

# windows

## Installation
For intalling Python download the suitable executable file from below:
- for `x86` download: [newest python version for x86](https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe)
- for `x64` download: [newest python version for x64](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe)
Run the downloaded file. (make sure to check the highlited box below for adding python path)
![install Python Win](docs/img/installPythonWin.png?raw=true "install Python Win")

### Using V-rep version 4 (CoppeliaSim)
[Download the installer_4.zip](https://github.com/Robocup-simplus/simplus_vrep/raw/master/easy_setup/windows/installer_v4.zip). Extract it and run the "installer_4.bat" by double clicking on it.

### Using V-rep version 3.6.2

Then, download V-rep from [coppeliarobotics](http://coppeliarobotics.com/files/V-REP_PLAYER_V3_6_2_Setup.exe), there is just a couple of Nexts to finish V-rep installation.

Afterwards, download `simplus_vrep-master` file from [Simplus Github](https://github.com/Robocup-simplus/simplus_vrep/archive/master.zip), and extract the downloaded file to the interested directory.

Run the bat file in `simplus_vrep-master/easy_setup/windows/install.bat` , to setup all the requirements(this setup includes prepared worlds, models, & etc, while the setup is finished you will be ask to press a key to exit).


## World setup

### Using V-rep version 4 (CoppeliaSim)

Run the bat file in `simplus_vrep-master/easy_setup/windows/simulator_v4.bat`.

### Using V-rep version 3.6.2
Run the bat file in `simplus_vrep-master/easy_setup/windows/simulator.bat` .

## Run 
There is two methods to communicate with the robot:
Approach1: is based on V-rep python API (there is no client and server & the robot controling code should be placed in the main function of `robotApi.py`.),
Approach2: is based on remote API (the teams should use `client.py` to control robot) 

> Remember to Stop the V-REP Simulator (by the V-REP Stop bottom) & Play agein (by the V-REP Start bottom) before starting a new Run.

### Approach1
- run `run1.bat`
### Approach 2
- run `run2_client.bat`
- run `run2-server.bat` 

---

# Ubuntu 16.04
## Installation
1. Download [Installer](https://github.com/Robocup-simplus/simplus_vrep/raw/master/easy_setup/ubuntu_16/installer.tar.gz)
2. Put the file where ever you want the simplus package be installed in.
3. Go to the interested folder, right click and open the terminal then write
   - Using V-rep version 4 (CoppeliaSim)
     ```bash
            sudo sh installer_v4.sh
     ```
   - Using V-rep version 3.6.2
     ```bash
            sudo sh installer.sh
     ```
4. Please press Y or Enter when ever the script asked.
## World setup
Go to the `simplus_vrep/easy_setup/ubuntu_16` directory, right click and open the terminal then write
   - Using V-rep version 4 (CoppeliaSim)
     ```bash
            sudo sh simulator_v4.sh
     ```
   - Using V-rep version 3.6.2
     ```bash
            sudo sh simulator.sh
     ```
## Run 
There is two methods to communicate with the robot:
Approach1: is based on V-rep python API (there is no client and server),
Approach2: is based on remote API (the teams should use client to control robot and the server is responnsible for other things prepared by technical committee) 

> Remember to Stop the V-REP Simulator (by the V-REP Stop bottom) & Play agein (by the V-REP Start bottom) before starting a new Run.

### Approach1
Go to the `simplus_vrep/easy_setup/ubuntu_16` directory, right click and open the terminal then write 
```bash
    sudo sh run1.sh
```

### Approach2
1. Go to the `simplus_vrep/easy_setup/ubuntu_16` directory, right click and open the terminal then write 
```bash
sudo sh run2_client.sh
```

2. Go to the `simplus_vrep/easy_setup/ubuntu_16` directory, right click and open the terminal then write 
```bash
sudo sh run2_server.sh`
```
---

# Ubuntu 18.04
## Installation
1. Download [Installer](https://github.com/Robocup-simplus/simplus_vrep/raw/master/easy_setup/ubuntu_18/installer.tar.gz)
2. Put the file where ever you want the simplus package be installed in.
3. Go to the interested folder, right click and open the terminal then write
   - Using V-rep version 4 (CoppeliaSim)
     ```bash
            sudo sh installer_v4.sh
     ```
   - Using V-rep version 3.6.2
     ```bash
            sudo sh installer.sh
     ```
4. Please press Y or Enter when ever the script asked.
## World setup
Go to the `simplus_vrep/easy_setup/ubuntu_18` directory, right click and open the terminal then write 
   - Using V-rep version 4 (CoppeliaSim)
     ```bash
            sudo sh simulator_v4.sh
     ```
   - Using V-rep version 3.6.2
     ```bash
            sudo sh simulator.sh
     ```
## Run 
There is two methods to communicate with the robot:
Approach1: is based on V-rep python API (there is no client and server),
Approach2: is based on remote API (the teams should use client to control robot and the server is responnsible for other things prepared by technical committee) 

> Remember to Stop the V-REP Simulator (by the V-REP Stop bottom) & Play agein (by the V-REP Start bottom) before starting a new Run.
### Approach1
Go to the `simplus_vrep/easy_setup/ubuntu_18` directory, right click and open the terminal then write 
```bash
sudo sh run1.sh
```

### Approach2
1. Go to the `simplus_vrep/easy_setup/ubuntu_18` directory, right click and open the terminal then write
```bash 
sudo sh run2_client.sh
```

2. Go to the `simplus_vrep/easy_setup/ubuntu_18` directory, right click and open the terminal then write 
```bash
sudo sh run2_server.sh
```

# Setup for Scratch
Based on your desired operating system go through steps abow and chose the **Approach2 & skip the client part** (since the client would be the Scratch program), then follow the below steps: 
1. Go to  https://scratchx.org/?url=https://Robocup-simplus.github.io/simplus.js#scratch  (wait till the extention loads)
2. Simplus blocks are located in "More Blocks" tab and you can drag and drop them to the right scene
3. In order to use the sample project, from the top menu click on  `File` then `load project` and select the `simplus_scratch.sbx` file from `simplus_vrep/client/scratch`

![Scratch sample code](docs/img/scratch.png?raw=true "Scratch Simplus extention")
