set PATH= %PATH%;C:\cygwin32\bin
cd ../..
cd client/cpp
g++ -c player_win.cc
g++ -static -o player.dll player_win.o
pause
