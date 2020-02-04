# Game_manager.ttm
the game manager panel which controls the server and scoreboard

# Floors
- floor_white.ttm
- floor_white_tiled.ttm
- infiniteFloor.ttm
- resizable floor 1-5 meters.ttm
- resizable floor 25-100 meters.ttm
- resizable floor 5-25 meters.ttm
    
# maze
- maze_1.ttm
  - a mazed model with the shaoe of a human brain
- maze_2.ttm
  - a circle maze
- maze_3.ttm
  - a smiley maze which also has been used in major virtual rescue


# obstacles
- heavy
  - blue, green, red, white, yellow, 
    - unmovable boxes
- light
  - blue, green, red, white, yellow, 
    - movable boxes
		
# robots
- simplus_e-puck.ttm
  - the e-puck modeled in v-rep with a monitoring and controling GUI.
  - the e-puck proximity max sensor range is 0.5 m. The proximity sensor return the distance between the robot and the obstacle.
  - the e-puck can move by setting the linear and angular speed. The linear speed is in range of (0,0.5) and the angular speed is in range of (0,1). exg: 0.5 means 90 degree and 1 means 180 degree.
  
# tiles
- speed_bump.ttm
  - a small speed bump model
- tile_black.ttm, tile_blue.ttm, tile_green.ttm, tile_red.ttm, tile_silver.ttm
  - different tiles are modeled with different rules such as check points, traps, or any other rules for penalties or scores.

# victims
- Victim_H_big.ttm, Victim_H_small.ttm, Victim_S._big.ttm, Victim_S_small.ttm, Victim_U_big.ttm, & Victim_U_small.ttm
  - H, U, & S markers are defined in order to cover rescue maze victims.
- Victim_lying.ttm, Victim_sitting.ttm, Victim_standing.ttm, Victim_walking.ttm
  - Four human victim model similar to the ones in virtual rescue major.
- Victim_ball_light_cyan.ttm, Victim_ball_light_pink.ttm, Victim_ball_light_red.ttm
  - Three ball victim model that the robot can move them.
- Victim_ball_heavy_cyan.ttm, Victim_ball__heavy_pink.ttm, Victim_ball__heavy_red.ttm
  - Three ball victim model that the robot can not move them.
		
# walls	
walls with different shapes and sizes are modeled.
- 10cm high walls
  - L wall.ttm, T wall.ttm, X wall.ttm, pillar 5cm.ttm, wall 12cm.ttm, wall 25cm.ttm, wall 2cm.ttm, wall 50cm.ttm, wall end.ttm
- 20cm high walls
  - L wall.ttm, T wall.ttm, X wall.ttm, pillar 10cm.ttm, wall end.ttm, wall section 100cm.ttm, wall section 25cm.ttm, wall section 50cm.ttm, wall section 5cm.ttm
