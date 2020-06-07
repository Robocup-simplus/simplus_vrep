#!/bin/bash

pwd
cd ../..
git pull
rm -f -R CoppeliaSim_Edu_V4_0_0_Ubuntu16_04/models/Simplus
mv models/Simplus/ CoppeliaSim_Edu_V4_0_0_Ubuntu16_04/models/
cp worlds/SampleMap.ttt  CoppeliaSim_Edu_V4_0_0_Ubuntu16_04/
sudo chmod 777 * -R
cd ..
sudo chmod 777 * simplus_vrep
