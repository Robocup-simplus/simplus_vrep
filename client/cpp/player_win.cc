#include <iostream>
#include <memory>
#include <string>
#include <stdlib.h>     /* abs */
#define EXPORT  __declspec(dllexport)
using namespace std;


int team_size,robot_per_team,color_sensor_size,proximity_sensor_size;

extern "C"{


EXPORT char *  start(int _team_size,int _robot_per_team,int _color_sensor_size,int _proximity_sensor_size){
	team_size=_team_size;
	robot_per_team=_robot_per_team;
	color_sensor_size=_color_sensor_size;
	proximity_sensor_size=_proximity_sensor_size;
	return "my_team_name";
}


EXPORT char * end(){
	return  "The Ending Message";

 	
}

EXPORT char* play(int colors_1[],int colors_2[],int colors_3[],int proximity_detected[],float proximity_distances[],float pos[],int *led_color_id,float *wheel_linear, float *wheel_angular,float * action_x,float * action_y,float * action_z){

    /* led_color_id: 1---> red  2---> green 3---> blue 4---> off
       colors_1[]: color sensor 1 value, colors are defined by (r,g,b), colors_1[0]-->r value  colors_1[1]-->g value colors_1[2]-->b value
       colors_1[]: color sensor 2 value, colors are defined by (r,g,b), colors_2[0]-->r value  colors_2[1]-->g value colors_3[2]-->b value
       colors_1[]: color sensor 3 value, colors are defined by (r,g,b), colors_3[0]-->r value  colors_2[1]-->g value colors_3[2]-->b value
       
       wheel_linear: linear velocity 
       wheel_angular: angular velocity
       
       proximity_distances[]: values of proximity sensor receptively, you can find the order numbers by clicking on each proximity sensor of robot model in model tree,vrep
       proximity_detected[]: the array length is equal to number of proximity sensor receptively and it's value is 0 or 1 for each proximity. 1 shows that the obstacle is detected
       
       pos[]: pos[0] --> x  pos[1] --> y   pos[2]--> z
       
       return char*: action name if action is detected or empty string
       action_x: the x position of the detected action
       action_y: the y position of the detected action
       action_z: the z position of the detected action
    */
    
    int color_sum_r = colors_1[0]+colors_2[0]+colors_3[0];
    int color_sum_g = colors_1[1]+colors_2[1]+colors_3[1];
    int color_sum_b = colors_1[2]+colors_2[2]+colors_3[2];

    if(color_sum_r>color_sum_g && color_sum_r> color_sum_b)
       *led_color_id = 1; //red
    else if(color_sum_g>color_sum_r && color_sum_g> color_sum_b)
        *led_color_id = 2; //green
    else if(color_sum_b>color_sum_r && color_sum_b> color_sum_g)
        *led_color_id = 3; //blue


    int  obstacle = 0;
    for (int i=1;i<5;i++)
        obstacle += proximity_detected[i];

    if (obstacle == 0){   //move forward
        *wheel_linear = 0.05;
        *wheel_angular = 0.0;
        }
    else{ //turn
        *wheel_linear = 0.0;
        *wheel_angular = 0.5;
    }

  if((colors_1[0]>100 && colors_1[0]<215 && colors_1[1]<215 && colors_1[2]<215 && abs(colors_1[0]-colors_1[1])<45 && abs(colors_1[1]-colors_1[2])<45 && abs(colors_1[0]-colors_1[2])<45 ) ||
     (colors_2[0]>100 && colors_2[0]<215 && colors_2[1]<215 && colors_2[2]<215 && abs(colors_2[0]-colors_2[1])<45 && abs(colors_2[1]-colors_2[2])<45 && abs(colors_2[0]-colors_3[2])<45 ) ||
     (colors_3[0]>100 && colors_3[0]<215 && colors_3[1]<215 && colors_3[2]<215 && abs(colors_3[0]-colors_3[1])<45 && abs(colors_3[1]-colors_3[2])<45 && abs(colors_3[0]-colors_3[2])<45 ))
    {
     *action_x = pos[0];
     *action_y = pos[1];
     *action_z = pos[2];
     return "find_checkpoint";
    }
  
  return "";

}

}

int main(){
	return 0;
}
