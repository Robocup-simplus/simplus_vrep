#!/bin/bash
ECHO Start Installing Simplus requirements
python get-pip.py
pip -V
pip install -r requirements.txt
CD ../../
CD worlds
copy SampleMap.ttt "C:\Program Files\V-REP3\V-REP_PRO_EDU\"
CD ..
CD models
Xcopy /E Simplus "C:\Program Files\V-REP3\V-REP_PRO_EDU\models\Simplus\"

PAUSE
