#!/bin/bash

sudo apt update
sudo apt-get install software-properties-commonng python-software-properties
sudo apt-get install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
sudo apt update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
sudo update-alternatives --config python
alias python=python3
sudo apt-get update
sudo apt install python-pip
sudo apt-get install curl
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python get-pip.py
sudo apt-get install git 
git clone "https://github.com/Robocup-simplus/simplus_vrep.git"
cd simplus_vrep/server
pip install -r requirements.txt
cd ..
curl -O http://www.coppeliarobotics.com/files/V-REP_PRO_EDU_V3_6_2_Ubuntu18_04.tar.xz
tar -xf  V-REP_PRO_EDU_V3_6_2_Ubuntu18_04.tar.xz
rm -f V-REP_PRO_EDU_V3_6_2_Ubuntu18_04.tar.xz
mv models/Simplus/ V-REP_PRO_EDU_V3_6_2_Ubuntu18_04/models/
cp worlds/SampleMap.ttt  V-REP_PRO_EDU_V3_6_2_Ubuntu18_04/
