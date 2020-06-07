#!/bin/bash

cd `dirname $0`
cd ../..
cd client/cpp
g++ -shared  player.cc -o player.dylib
python client.py
