#!/bin/bash

cd ../..
cd client/cpp
g++ -fPIC player.cc -shared  -o player.so
