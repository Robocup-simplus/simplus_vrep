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
The simplus team made the game's rules flexible by defining Two config files. These files will ease the Technical Committee's work By letting them make improvements in league each year without changing the server code. 

### serverconfig
Server Configuration can be set using `server/serverconfig.txt`. This Configuration will define the available actions in server inorder to define each game's rule. You can define as many actions as you want. Each line will define a new action, each action will be defined using 6 characteristics. The first term of characteristic is the Action's name which will be sent with the estimated position by the client in order to announce their percptions of Action in a position to get scores. The second characteristic is the list of model's names(Can be found in Vrep's Scene Hierachy) that are involved in the Action.The third characteristic is the list of number of each involved model respectively. Next characteristic is the Action's range in meter which defines the maximum acceptable distance between the position that the team claimed for the Action and the real position of the nearest model defined in the action. The two next characteristics are the positive and negetive scores of the action. Positive score is the score team will recieve if the distance was acceptable and the negetive score is the score that will affect the team's core if the distance was greater. The negetive score can be set to zero.
   - Action1's name;List of Action1's models;List of number of each Action1's model;Action1's range;Action1's Positive score ;Action1's Negetive score
   - Action2's name;List of Action2's models;List of number of each Action2's model;Action2's range;Action2's Positive score ;Action2's Negetive score

Sample `serverconfig.txt`:
```
action1;Cuboid,Cylinder;6,4;10;5;-1
```

### trapconfig
Trap Configuration can be set using `server/trapconfig.txt`. This Configuration will define the actions that the server will automatically check each cycle of the game. Most of the times, these actions will be used to define some limitation in the game and decreasing the team's score. You can define as many traps as you want. Each line will define a new trap. 

- Trap1's name;List of Trap1's models;List of number of each Trap1's model;Trap1's range;Trap1's offset ;Trap1's score
- Trap2's name;List of Trap2's models;List of number of each Trap2's model;Trap2's range;Trap2's offset ;Trap2's score

Sample `trapconfig.txt`:
```
trap1;Cuboid;6;2;0.1;-2
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
