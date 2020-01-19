#!/bin/bash

cd `dirname $0`
pwd
cd ../..
git pull
rm -f -R V-REP_PRO_EDU_V3_6_2_Mac/models/Simplus
mv models/Simplus/ V-REP_PRO_EDU_V3_6_2_Mac/models/
cp worlds/SampleMap.ttt  V-REP_PRO_EDU_V3_6_2_Mac/vrep.app/Contents/MacOS/

pwd
