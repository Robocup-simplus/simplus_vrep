#!/bin/bash

cd `dirname $0`
cd ../
cd client/cpp
g++ -I /usr/local/include/opencv4/ -std=c++11 -shared  -o player.dylib player.cc -lopencv_core -lopencv_imgcodecs -lopencv_imgproc -lopencv_highgui
g++ -shared  player.cc -o player.dylib
python client.py
