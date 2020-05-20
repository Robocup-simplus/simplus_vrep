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
sudo apt install python3-pip
sudo apt-get install curl
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python get-pip.py
sudo apt-get install git 
git clone "https://github.com/Robocup-simplus/simplus_vrep.git"
cd simplus_vrep/server
pip install -r requirements.txt
cd ..
wget http://www.coppeliarobotics.com/files/CoppeliaSim_Edu_V4_0_0_Ubuntu16_04.tar.xz 
tar -xf  CoppeliaSim_Edu_V4_0_0_Ubuntu16_04.tar.xz
rm -f CoppeliaSim_Edu_V4_0_0_Ubuntu16_04.tar.xz
mv models/Simplus/ CoppeliaSim_Edu_V4_0_0_Ubuntu16_04/models/
cp worlds/SampleMap.ttt  CoppeliaSim_Edu_V4_0_0_Ubuntu16_04/
sudo chmod 777 * -R
cd ..
sudo chmod 777 * simplus_vrep
sudo apt-get install python3-tk
sudo apt-get install python3-apt
sudo apt-get install python3-pil python3-pil.imagetk
pip install -U Pillow


