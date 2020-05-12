
# pip install tkfilebrowser
# pip install image

from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import os 
import uuid
import time
import math
import _thread
import pathlib

import platform
import subprocess

root = Tk()
root.title("Robocup Simplus Panel")



def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"

os_type='mac'
is_32=False
if platform.system() =='cli':
        os_type = 'windows'
elif platform.system() =='Windows':
        os_type = 'windows'
elif platform.system() == 'Darwin':
        os_type = 'mac'
elif platform.system() == 'Linux':
    if linux_distribution() == "N/A" :
      os_type = 'ubuntu_18'
    elif linux_distribution()[1] == '16.04':
        os_type = 'ubuntu_16'
    else:
        os_type = 'ubuntu_18'
else:
       os_type = 'windows' 
       is_32=True 



def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#base_path = str(pathlib.Path(__file__).parent.absolute())
# if base_path == '':
#    base_path=resource_path("")

base_path=resource_path("")
if os_type == 'mac':
  base_path=base_path.replace('Simplus.app/Contents/MacOS/','')

address=base_path.split('/')
if len(address)<2:
  address=base_path.split('\\')

postfix=len(address[-2])+1
base_path = base_path[:-1*postfix]




def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    return proc_stdout

def simulator_th():
  if  os_type == 'windows':
       #subprocess_cmd("cd "+base_path+"simulator & coppeliaSim.exe -s -q SampleMap.ttt")
      subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+"simulator_v4.bat")
  else:
      subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"simulator_v4.sh")


def simulator():
  try:
    _thread.start_new_thread( simulator_th, ( ) )

  except Exception as e:
    print(e)
    return
def run_client_th():
  print("run client")
  if  os_type == 'windows':
      if lang_var.get()==2:
           subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+" run2_client_cpp.bat")
      elif  lang_var.get()==3:
          msg_var.set("Please Double Click on your scratch program");
      else:
           subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+" run2_client.bat")
  else:
      if lang_var.get()==2:
          subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"run2_client_cpp.sh")
      elif  lang_var.get()==3:
          msg_var.set("Please Double Click on your scratch program");
      else:
          subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"run2_client.sh")


def run_client():
  try:
    _thread.start_new_thread( run_client_th, ( ) )

  except Exception as e:
    print(e)
    return


def run_server_th():
    print("run server")
    if  os_type == 'windows':
      subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+"run2_server.bat")
    else:
      subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"run2_server.sh")


def run_server():
  try:
    _thread.start_new_thread( run_server_th, ( ) )

  except Exception as e:
    print(e)

def clear_th():
  print("clear")
  if os_type == 'windows':
      subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+"clear.bat")
  else:
      subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"clear.sh")


def clear():
  try:
    _thread.start_new_thread( clear_th, ( ) )

  except Exception as e:
    print(e)

def code_compile_th():
  print("compile")
  if  os_type == 'windows':
      if lang_var.get()==2:
         if is_32:
           msg_var.set(str(subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+"compile_cpp_32.bat")))
         else:
          msg_var.set(str(subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+"compile_cpp_64.bat")))
      elif  lang_var.get()==3:
          msg_var.set("Please Double Click on your scratch program");
      else:
          msg_var.set(str( subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+" run2_client.bat")))
          clear()     
  else:
     if lang_var.get()==2:
         msg_var.set(str(subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"compile_cpp.sh")))
     elif  lang_var.get()==3:
          msg_var.set("Please Double Click on your scratch program");
     else:
          msg_var.set(str(subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"run2_client.sh")))
          clear()     


def code_compile():
  try:
    _thread.start_new_thread( code_compile_th, ( ) )

  except Exception as e:
    print(e)

def choose():
    msg_var.set("")
    file_name_var.set("")
    
    txt.delete(0, END)
    txt.insert(0, "")
    address=root.filename = askopenfilename(filetypes=(("python files","*.py"),("c files","*.c"),("cpp files","*.cpp"),("cpp files","*.cc") )) 
    
    n = -1;
    for i in range(len(address)-1,0,-1):
       if address[i]== "/" or address[i]== "\\" :
            n=i;
            break;
    
    if n == -1:
        return;  
    
    print(address)
    file_name_var.set(address)
    txt.insert(0,address)


def copy_file(destination,f1):
    f = open(destination, 'wb')
    data=bytearray(f1.read())
    f.write(data)
    f.close()


def show_progress():
 msg_var.set("Uploading ....");
 try:
    f1=open(str(file_name_var.get()), 'rb')
    if lang_var.get()==2:
        destination = base_path + 'client/cpp/'
        copy_file(destination+"player.cc",f1)
        copy_file(destination+"player_win.cc",f1)
    else:
        destination = base_path + 'client/python/player.py'
        copy_file(destination,f1)

    f1.close()

    msg_var.set("Code is uploaded successfully!")
 except Exception as e:
    print("ERROR",e)
    return


def upload():
  try:
    _thread.start_new_thread( show_progress, ( ) )

  except Exception as e:
    print(e)
    return

########################
file_name_var = StringVar(root)
file_name = Label(root, textvariable=file_name_var)
file_name.visible = False


########################

# logo

img =  PhotoImage(file = resource_path("../docs/icons/logo.gif") )
imglabel = Label(root, image=img).grid(row=0,column=0,columnspan=3)        


# Creating a photoimage object to use image 
# photo_install = PhotoImage(file = r"test.gif") 
  
# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
# btn_install=Button(root, text = 'Start Intallation!', image = photo_install, compound = LEFT)
# btn_install.grid(row=1,column=0, pady=(15, 15),columnspan=3)


def changedes():
	print(str(lang_var.get()))

# change destination
lang_var = StringVar(root, "1") 
  
Radiobutton(root, text = "Python", variable = lang_var,command=changedes,value = 1, indicator = 0,width=8).grid( row=2,column=0 ) 
Radiobutton(root, text = "C/C++", variable = lang_var,command=changedes,value = 2, indicator = 0,width=8).grid(row=2,column=1) 
Radiobutton(root, text = "Scratch", variable = lang_var, command=changedes,value = 3, indicator = 0,width=8).grid(row=2,column=2) 


# msg
title_var = StringVar(root)
title = Label(root, textvariable=title_var,width=15)
title.grid(row=3,column=0, padx=(15, 0), pady=(40, 0))
title.visible = True
title_var.set("Change Client code:");

# choose file 
txt = Entry(root,width=20)
txt.grid(row=4,column=0, columnspan=2,pady=(20, 0),padx=(10, 0))
btn = Button(root, text="Choose file", command=choose,width=10)
btn.grid(row=4,column=2,pady=(20, 0))


#start encode
btn = Button(root, text="Upload", command=upload,width=10)
btn.grid(row=5,column=0, pady=(10, 0), columnspan=3)

# msg
msg_var = StringVar(root)
msg = Label(root, textvariable=msg_var)
msg.grid(row=6,column=1, columnspan=3, padx=(60, 0), pady=(15, 0))
msg.visible = True
# msg_var.set(base_path)


# Creating a photoimage object to use image 
photo_sim = PhotoImage(file = resource_path("../docs/icons/sim.gif")) 
  
# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn_sim=Button(root, text = 'Open Simulator!', image = photo_sim, compound = LEFT,command=simulator)
btn_sim.grid(row=7,column=0, pady=(15, 0),columnspan=3)



# Creating a photoimage object to use image 
photo_compile = PhotoImage(file = resource_path("../docs/icons/comp.gif"))
  
# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn_compile=Button(root, text = '    Compile!       ', image = photo_compile, compound = LEFT,command=code_compile)
btn_compile.grid(row=8,column=0, pady=(15, 0),columnspan=3)


# Creating a photoimage object to use image 

photo_clear = PhotoImage(file = resource_path("../docs/icons/clear.gif") )
  
# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn_clear=Button(root, text = '        Clear!        ', image = photo_clear, compound = LEFT,command=clear)
btn_clear.grid(row=9,column=0, pady=(15, 0),columnspan=3)

# Creating a photoimage object to use image 
photo_run_client = PhotoImage(file = resource_path("../docs/icons/run_client.gif") )
photo_run_server = PhotoImage(file = resource_path("../docs/icons/run_server.gif") )
  
# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn_run=Button(root, text = '    Run Client!    ', image = photo_run_client, compound = LEFT,command=run_client)
btn_run.grid(row=10,column=0, pady=(15, 0),columnspan=3)


btn_run=Button(root, text = '    Run Server!   ', image = photo_run_server, compound = LEFT,command=run_server)
btn_run.grid(row=11,column=0, pady=(15, 0),columnspan=3)





root.mainloop()


