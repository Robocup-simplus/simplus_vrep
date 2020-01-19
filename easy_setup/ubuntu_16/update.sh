#!/bin/bash

pwd
cd ../..
git pull
rm -f -R V-REP_PRO_EDU_V3_6_2_Ubuntu16_04/models/Simplus
mv models/Simplus/ V-REP_PRO_EDU_V3_6_2_Ubuntu16_04/models/
cp worlds/SampleMap.ttt  V-REP_PRO_EDU_V3_6_2_Ubuntu16_04/
sudo chmod 777 * -R
cd ..
sudo chmod 777 * simplus_vrep
