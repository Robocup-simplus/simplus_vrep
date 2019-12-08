# VREP Installation
Go to official download page of V-Rep: [Coppelia Robotics](http://www.coppeliarobotics.com/previousVersions)
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
curl -O http://www.coppeliarobotics.com/files/V-REP_PRO_EDU_V3_6_2_Ubuntu18_04.tar.xz
tar -xzfv V-REP_PRO_EDU_V3_6_2_Ubuntu18_04.tar.xz
cd V-REP_PRO_EDU_V3_6_2_Ubuntu18_04
./vrep.sh
```

---

# Server Installation
1.  Clone or Download the project.
2.  Move `models/SimPlus` directory to vrep `models` directory.
3.  Install [`python3.5+`](https://www.python.org/downloads/) and [`pip`](https://pip.pypa.io/en/stable/installing/) (In windows don't forget to click on 'Add python to PATH' and 'Install pip' checkbox in the installation process. In case you forgot to check those you have to install python again or config those setting manually using the Tutorial for Windows [Link](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation))
4.  Go to server directory and run `pip install -r requirements.txt`
---

# Server Setup
The simplus team made the game's rules flexible by defining Two config files. These files will ease the Technical Committee's work By letting them make improvements in league each year without changing the server code. 

### serverconfig
Server Configuration can be set using `server/serverconfig.txt`. This Configuration will define the available actions in server inorder to define each game's rule. You can define as many actions as you want. Each line will define a new action and each action will be defined using 6 characteristics.

```
  - Action1's name;List of Action1's models;List of number of each Action1's model;Action1's range;Action1's Positive score ;Action1's Negetive score
  - Action2's name;List of Action2's models;List of number of each Action2's model;Action2's range;Action2's Positive score ;Action2's Negetive score
```

- The first characteristic is the Action's name which will be sent with the estimated position by the client in order to announce their percptions of Action in a position to get scores.
- The second characteristic is the list of model's names(Can be found in Vrep's Scene Hierachy) that are involved in the Action.
- The third characteristic is the list of number of each involved model respectively. 
- The forth characteristic is the Action's range in meter which defines the maximum acceptable distance between the position that the team claimed for the Action and the real position of the nearest model defined in the action. 
- Positive score is the score team will recieve if the distance was acceptable and the negetive score is the score that will affect the team's core if the distance was greater. It should be mentioned that the negetive score can be set to zero.
 
Sample `serverconfig.txt`:
```
action1;Cuboid,Cylinder;6,4;10;5;-1
```

### trapconfig
Trap Configuration can be set using `server/trapconfig.txt`. This Configuration will define the actions that the server will automatically check each cycle of the game. Most of the times, these actions will be used to define some limitation in the game and decreasing the team's score. You can define as many traps as you want. Each line will define a new trap and each trap will be defined using 6 characteristics.

```
- Trap1's name;List of Trap1's models;List of number of each Trap1's model;Trap1's range;Trap1's offset ;Trap1's score
- Trap2's name;List of Trap2's models;List of number of each Trap2's model;Trap2's range;Trap2's offset ;Trap2's score
```

- The first characteristic is the Traps's name which will be used in the server log inorder to show the final result's calculation.
- The second characteristic is the list of model's names(Can be found in Vrep's Scene Hierachy) that are involved in the Trap.
- The third characteristic is the list of number of each involved model respectively.
- The forth characteristic is the Action's range in meter will be combined with the trap's offset and defines weather the robot is fall in the trap or not. In other words it's the minimum distance between the robot's position and the real position of the nearest model defined in the trap with offset considration.
- The Trap's score is the score that the robot will recieve if it's position meats the afformentioned condition. It should be mentioned that although the config file is named as "trap" by setting the score a positive number, it can also be used as reward.
 
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


---

# Usage
- Open the Vrep Simulator (Make sure about the setup using [VREP Installation ](MANUAL_SETUP.md))
- From the top menu click on  `File` then `Open Scene` and select the `SampleMap.ttt` file from `simplus_vrep/worlds`
- Run the VREP and Start the world (click on play icon)

## Python 

### Approach 1
Run the robotApi, in this approach the client code should be placed in the main function of "robotApi.py". The client can directly access the provided python functions that are declared in the same file. It should be mentioned that this approach is the core part of the second approach. (Go to  `simplus_vrep/server` directiory):
```bash
python robotApi.py 
```

### Approach 2
In this approach, the client file is writen in a template that makes the development and game management much easier for both students and Technical committies. 
1. Run Clients (Go to  `simplus_vrep/client/python` directiory):
```bash
python client.py
```
2. Run Servers for each client (Go to  `simplus_vrep/server` directiory):
```bash
python server.py
```
4. Manage the Game using the Game manager GUI, The Game will start after pressing it's "play" button.

5. Manage and Watch the Game form Lua Panel 

![SimPlus on macOS](docs/img/full.png?raw=true "Simplus on macOS")

## Scratch 
1. Run Server (Go to  `simplus_vrep/server` directiory):
```bash
python simplus_scratch.py
```
2. Go to  https://scratchx.org/?url=https://Robocup-simplus.github.io/simplus.js#scratch  (It may takes few minutes)
3. Simplus blocks are located in "More Blocks" tab and you can drag and drop them to the right scene
4. In order to use the sample project, from the top menu click on  `File` then `load project` and select the `simplus_scratch.sbx` file from `simplus_vrep/client/scratch`

![Scratch sample code](docs/img/scratch.png?raw=true "Scratch Simplus extention")


