FOR /F "tokens=4 delims= " %%P IN ('netstat -a -n -o ^| findstr :8080') DO @ECHO TaskKill.exe /PID %%P
FOR /F "tokens=4 delims= " %%P IN ('netstat -a -n -o ^| findstr :50051') DO @ECHO TaskKill.exe /PID %%P
