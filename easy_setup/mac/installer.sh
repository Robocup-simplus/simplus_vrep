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
cd simplus_vrep/server
pip install -r requirements.txt
cd ..
wget "http://www.coppeliarobotics.com/files/V-REP_PRO_EDU_V3_6_2_Mac.zip"
unzip V-REP_PRO_EDU_V3_6_2_Mac.zip
rm -f V-REP_PRO_EDU_V3_6_2_Mac.zip
cd ..
rm -f installer.sh
rm -f get-pip.py
rm -f distribute_setup.py