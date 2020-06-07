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

### Game manager
In order to add the "Game manager" to the world, you should drag & drop the game_manager.ttm in your Scene.
It should be mention that game_manager.ttm  could be found in the "Model browser" section of V-rep and in the root of "Simplus" directory.
For setting the "game duration" in "Cycle" format:
  1. open the "Scene Hirarchy" section of V-rep 
  2. find the "Game_manager" model
  3. Double click on the "script icon" near the "Game_manager"
  4. Go to Line 130 and change the "game_duration" variable(It's default value is 1000)
  ```bashe
    -- Set game duration here --
    game_duration=1000;
  ```
  5. press the following key coresspond to your OS inorder to save the script
      - ctrl+ s (Windows/Ubuntu)
      - command + s (mac)
  6. close the script
