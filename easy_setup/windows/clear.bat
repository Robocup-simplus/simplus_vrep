FOR /F "tokens=4 delims= " %%P IN ('netstat -a -n -o ^| findstr :8080') DO  taskkill /PID %%P /F
FOR /F "tokens=4 delims= " %%P IN ('netstat -a -n -o ^| findstr :4719') DO  taskkill /PID %%P /F
FOR /F "tokens=5 delims= " %%P IN ('netstat -a -n -o ^| findstr :8080') DO  taskkill /PID %%P /F
FOR /F "tokens=5 delims= " %%P IN ('netstat -a -n -o ^| findstr :4719') DO  taskkill /PID %%P /F
CD ../../
del /f client_log.txt
PAUSE
