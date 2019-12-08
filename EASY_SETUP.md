Follow the setup instruction based on your OS:
- [macOS](#macOS)
  - [macOS Installation](https://github.com/Robocup-simplus/simplus_vrep/blob/master/EASY_SETUP.md#installation)
  - [World setup](https://github.com/Robocup-simplus/simplus_vrep/blob/master/EASY_SETUP.md#world-setup)
  - [Run](https://github.com/Robocup-simplus/simplus_vrep/blob/master/EASY_SETUP.md#run)
    - [Approach 1](https://github.com/Robocup-simplus/simplus_vrep/blob/master/EASY_SETUP.md#approach1)
    - [Approach 2](https://github.com/Robocup-simplus/simplus_vrep/blob/master/EASY_SETUP.md#approach2)
- [Windows](#Windows)
  - [Windows Installation](https://github.com/Robocup-simplus/simplus_vrep/blob/master/EASY_SETUP.md#installation-1)
  
---

# macOS  
## Installation
1. Download [Installer.sh](https://raw.githubusercontent.com/Robocup-simplus/simplus_vrep/master/easy_setup/mac/installer.sh)
2. Put the file where ever you want the simplus package be installed in(The destination folder name should not include any spaces like " ").
3. Open the terminal and write `sh `
4. Drag and drop the `Installer.sh` file to terminal.
5. Press enter
6. At the end of the installation the installation path will be printed and if it is different with your interested folder you can easily cut the  `simplus_vrep` folder and place it where ever you want. 
- In case you face any error download [Installer_full.sh](https://raw.githubusercontent.com/Robocup-simplus/simplus_vrep/master/easy_setup/mac/installer_full.sh) and repeat step 3 to 5.

## World setup
- Open the terminal and right `sh `
- Drag and drop the `simulator.sh` file to terminal.(It can be found in `simplus_vrep/easy_setup/mac` directory)
- Press enter

## Run 
There is two methods to communicate with the robot:
Approach1: is based on V-rep python API (there is no client and server),
Approach2: is based on remote API (the teams should use client to control robot and the server is responnsible for other things prepared by technical committee) 

### Approach1
- Open Another terminal and write `sh `
- Drag and drop the `run1.sh` file to terminal.(It can be found in `simplus_vrep/easy_setup/mac` directory)
- Press enter
### Approach 2
- Open Another terminal and write `sh `
- Drag and drop the `run2.sh` file to terminal.(It can be found in `simplus_vrep/easy_setup/mac` directory)
- Press enter

---

# windows

## Installation
For intalling Python download the suitable executable file from below:
- for `x86` download: [newest python version for x86](https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe)
- for `x64` download: [newest python version for x64](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe)
Run the downloaded file. (make sure to check the highlited box below for adding python path)
![install Python Win](docs/img/installPythonWin.png?raw=true "install Python Win")

Then, download V-rep from [coppeliarobotics](http://coppeliarobotics.com/files/V-REP_PLAYER_V3_6_2_Setup.exe), there is just a couple of Nexts to finish V-rep installation.

Afterwards, download `simplus_vrep-master` file from [Simplus Github](https://github.com/Robocup-simplus/simplus_vrep/archive/master.zip), and extract the downloaded file to the interested directory.

Run the bat file in `simplus_vrep-master/easy_setup/windows/install.bat` **as administrator**, to setup all the requirements(this setup includes prepared worlds, models, & etc, while the setup is finished you will be ask to press a key to exit).


## World setup
Run the bat file in `simplus_vrep-master/easy_setup/windows/simulator.bat` **as administrator** to open and setup the world.

## Run 
There is two methods to communicate with the robot:
Approach1: is based on V-rep python API (there is no client and server & the robot controling code should be placed in the main function of `robotApi.py`.),
Approach2: is based on remote API (the teams should use `client.py` to control robot) 

### Approach1
- run `run1.bat`
### Approach 2
- run `run2_client.bat`
- run `run2-server.bat` 

---

# Ubuntu 16.04
## Installation
1. Download [Installer.sh](https://raw.githubusercontent.com/Robocup-simplus/simplus_vrep/master/easy_setup/ubuntu_16/installer.sh)
2. Put the file where ever you want the simplus package be installed in(The destination folder name should not include any spaces like " ").
3. Go to the interested folder, right click and open the terminal then write `sh installer.sh`
4. Please press Y or Enter when ever the script asked.
## World setup
Go to the `simplus_vrep/easy_setup/ubuntu_16` directory, right click and open the terminal then write `sh simulator.sh`
## Run 
### Approach1
Go to the `simplus_vrep/easy_setup/ubuntu_16` directory, right click and open the terminal then write `sh run1.sh`
### Approach2
Go to the `simplus_vrep/easy_setup/ubuntu_16` directory, right click and open the terminal then write `sh run2.sh`

---

# Ubuntu 18.04
## Installation
1. Download [Installer.sh](https://raw.githubusercontent.com/Robocup-simplus/simplus_vrep/master/easy_setup/ubuntu_18/installer.sh)
2. Put the file where ever you want the simplus package be installed in(The destination folder name should not include any spaces like " ").
3. Go to the interested folder, right click and open the terminal then write `sh installer.sh`
4. Please press Y or Enter when ever the script asked.
## World setup
Go to the `simplus_vrep/easy_setup/ubuntu_18` directory, right click and open the terminal then write `sh simulator.sh`
## Run 
### Approach1
Go to the `simplus_vrep/easy_setup/ubuntu_18` directory, right click and open the terminal then write `sh run1.sh`
### Approach2
Go to the `simplus_vrep/easy_setup/ubuntu_18` directory, right click and open the terminal then write `sh run2.sh`


