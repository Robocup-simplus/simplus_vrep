#!/bin/bash
pid=$(lsof -ti tcp:8080)
if [ $pid ]; then
  kill -9 $pid
fi

pid=$(lsof -ti tcp:4719)
if [ $pid ]; then
  kill -9 $pid
fi

cd ../../logs
rm -f client_log.txt
