#!/bin/bash
ECHO Start Installing Simplus requirements
powershell -Command [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; "Invoke-WebRequest https://github.com/Robocup-simplus/simplus_vrep/archive/master.zip -OutFile Simplus.zip"
powershell Expand-Archive Simplus.zip
CD Simplus/simplus_vrep-master/easy_setup/windows
python get-pip.py
pip -V
pip install -r requirements.txt
CD ../../
powershell -Command [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;  "Invoke-WebRequest http://www.coppeliarobotics.com/files/CoppeliaSim_Edu_V4_0_0_Win.zip -OutFile simulator.zip"
powershell Expand-Archive simulator.zip
copy "worlds\SampleMap.ttt" "simulator\"
Xcopy /E "models" "simulator\models"
PAUSE
