# SimPlus_VRep
This repository is dedicated to a Rescue simulation environment for Robocup Juniors and is aimed to be a bridge from Robocup Junior Rescue to Robocup Major Rescue competitions.


# VREP Installation
Go to official download page of V-Rep: [Coppelia Robotics](http://www.coppeliarobotics.com/downloads.html)
## Windows
Download `V-REP PRO EDU V3.6.2 rev0` and execute `V-REP_PRO_EDU_V3_6_2_Setup.exe`

## MacOs
Download `V-REP PRO EDU V3.6.2 rev0` and unzip `V-REP_PRO_EDU_V3_6_2_Mac.zip` then execute `vrep.app`

In case you find your "model browser" empty you may need to use the following commands:

```
cd V-REP_PRO_EDU_V3_6_2_Mac 
vrep.app/Contents/MacOS/vrep
```

## Linux (Only Ubuntu 16.04 / 18.04)
Download `V-REP PRO EDU V3.6.2 rev0` and extract `V-REP_PRO_EDU_V3_6_2_Mac.tar.gz` then execute `vrep`

or Use Terminal

Ubuntu 16.04:
```bash
curl -O http://www.coppeliarobotics.com/files/V-REP_PRO_EDU_V3_6_2_Ubuntu16_04.tar.xz
tar -xzfv V-REP_PRO_EDU_V3_6_2_Ubuntu16_04.tar.xz
cd V-REP_PRO_EDU_V3_6_2_Ubuntu16_04
./vrep.sh
```

Ubuntu 18.04:
```bash
curl -O http://www.coppeliarobotics.com/files/V-REP_PRO_EDU_V3_6_2_Ubuntu16_04.tar.xz
tar -xzfv V-REP_PRO_EDU_V3_6_2_Ubuntu16_04.tar.xz
cd V-REP_PRO_EDU_V3_6_2_Ubuntu16_04
./vrep.sh
```

---

# Server Installation
1.  Clone or Download the project.
2.  Move `models/SimPlus` directory to vrep `models` directory.
3.  Install [`python3.5+`](https://www.python.org/downloads/) and [`pip`](https://pip.pypa.io/en/stable/installing/) (Tutorial for Windows [Link](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation))
4.  Go to server directory and run `pip install -r requirements.txt`
---

# Server Setup
All Configuration can be set in `serverconfig.txt`

---

# Client Setup
### Python
1.  Install [`python3.5+`](https://www.python.org/downloads/) and [`pip`](https://pip.pypa.io/en/stable/installing/) (Tutorial for Windows [Link](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation))
2.  Go to client directory and run `pip install -r requirements.txt`

### Scratch
In order to access the sctrachx extension project, one should do one of the followings:
- using the link to open the project: https://scratchx.org/?url=https://Robocup-simplus.github.io/simplus.js#scratch
- Downloading the files and opening the "simplus_scratch.sbx" file in http://scratchx.org/ by "Open Extension File" and browsing the "simplus_scratch.sbx" file. (The sctrachx project uses Adobe Flashplayer so you should allow the website to run the progrom.)
- Loading the "simplus_scratch.sbx" file by browing from https://scratchx.org/#scratch and File > Load Projects.

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
