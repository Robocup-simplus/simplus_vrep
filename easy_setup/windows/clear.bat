#!/bin/bash
FOR /F "tokens=4 delims= " %%P IN ('netstat -a -n -o ^| findstr :8080') DO @ECHO TaskKill.exe /PID %%P
FOR /F "tokens=4 delims= " %%P IN ('netstat -a -n -o ^| findstr :4719') DO @ECHO TaskKill.exe /PID %%P
CD ../../
del /f client_log.txt
PAUSE
