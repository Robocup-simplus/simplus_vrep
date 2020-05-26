#!/bin/bash

cd ../..
python client/python/client.py & 
cd server; python server.py

