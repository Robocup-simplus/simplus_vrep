#!/bin/bash

cd `dirname $0`
pwd
brew install python
curl -O http://python-distribute.org/distribute_setup.py
unlink /usr/local/bin/python
alias python='python3.7'
ln -s /usr/local/bin/python3.7 /usr/local/bin/python
python distribute_setup.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
brew install git
git clone "https://github.com/Robocup-simplus/simplus_vrep.git"
cd simplus_vrep/easy_setup/mac
pip install -r requirements.txt
cd ../..
brew install wget
wget "http://www.coppeliarobotics.com/files/CoppeliaSim_Edu_V4_0_0_Mac.zip"
unzip CoppeliaSim_Edu_V4_0_0_Mac.zip
rm -f CoppeliaSim_Edu_V4_0_0_Mac.zip
mv models/Simplus/ CoppeliaSim_Edu_V4_0_0_Mac/models/
cp worlds/SampleMap.ttt  CoppeliaSim_Edu_V4_0_0_Mac/
cd ..
rm -f installer_v4.sh
rm -f get-pip.py
rm -f distribute_setup.py
pwd
