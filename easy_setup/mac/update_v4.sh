#!/bin/bash

cd `dirname $0`
pwd
cd ../..
git pull
rm -f -R CoppeliaSim_Edu_V4_0_0_Mac/models/Simplus
mv  models/Simplus/ CoppeliaSim_Edu_V4_0_0_Mac/models/ 
cp worlds/SampleMap.ttt  CoppeliaSim_Edu_V4_0_0_Mac/

pwd
