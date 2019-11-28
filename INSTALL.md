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
Download `V-REP PRO EDU V3.6.2 rev0` and extract `V-REP_PRO_EDU_V3_6_2_Mac.tar.gz` then execute `vrep.sh`

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
All Configuration can be set in `server/serverconfig.txt` . This Configuration will describe the rules of each game. 
   - Action1's name;List of Action1's models;List of number of each Action1's model;Action1's Positive score ;Action1's Negetive score
   - Action2's name;List of Action2's models;List of number of each Action2's model;Action2's Positive score ;Action2's Negetive score

Sample `serverconfig.txt`:
```
action1;Cuboid,Cylinder;6,4;10;5;-1
```
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
