#include <iostream>
#include <memory>
#include <string>

#include <grpcpp/grpcpp.h>

#include "simplus.grpc.pb.h"

using SimPlus::WorldInfo;
using SimPlus::ServerInfo;
using SimPlus::TeamInfo;
using SimPlus::Observations;
using SimPlus::Observation;
using SimPlus::Proximity;
using SimPlus::Position;
using SimPlus::Commands;
using SimPlus::Command;
using SimPlus::Ending;
using SimPlus::Result;
using SimPlus::Action;
using SimPlus::CheckPoint;
using SimPlus::Pixel;
using SimPlus::Image;
using simplus=SimPlus::SimPlus;


WorldInfo info=WorldInfo();



void start(const WorldInfo* worldInfo,TeamInfo* teamInfo){

     info=*worldInfo;
     teamInfo->set_name( "my_team_name");

  }

  void end(const Ending* ending,Result* result)  {
  	result->set_message( "The Ending Message");
  
  } 
  void play(int id,ServerInfo server,Observation observation,Command* command) {

	//change led
	std::string col[4] = {"red", "green", "blue", "akldjf"};
    int a[3] = {0, 0, 0};
    for (Pixel c :observation.colors()){
        a[0] += c.r();
        a[1] += c.g();
        a[2] += c.b();
    }
    if( a[0]>a[1] && a[0]> a[2]) 
	    command->set_led(col[0]);
	else if( a[1]> a[0] && a[1]> a[2]) 
	    command->set_led(col[1]);
	else
		command->set_led(col[2]);
	//move
    int obstacle = 0;
    int i=0;
    for(Proximity proximity :observation.distances()){
        obstacle += proximity.detected();

    	if (obstacle == 0){
        	command->set_linear(0.05);
   		    command->set_angular(0.0);
   	     }
    	else{
    		if(i<5){
       	  		command->set_linear(0.0);
            	command->set_angular(-0.5);
            }
            else{
                command->set_linear(0.0);
            	command->set_angular(0.5);  
            }
	     }
	    i++;
    }
   //action
    for (Pixel c : observation.colors()){
       if(c.r()>100 and c.r()<215 and c.g()<215 and c.b()<215 and abs(int(c.r())-int(c.g()))<45 and abs(int(c.g())-int(c.b()))<45 and  abs(int(c.r())-int(c.b()))<45 ){
           Action* act=command->add_actions();
           act->set_x(observation.pos().x());
           act->set_y(observation.pos().y());
           act->set_z(observation.pos().z());
           act->set_type("find_checkpoint");
           break;
        }
    }
    
  }
  
 



