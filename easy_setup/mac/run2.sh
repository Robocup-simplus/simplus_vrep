#!/bin/bash

cd `dirname $0`
cd ../..
python client/python/client.py & 
cd server; python server.py
