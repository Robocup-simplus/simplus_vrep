#pip install wxpython
#----------------------------------------------------------------------
# A very simple wxPython example.  Just a wx.Frame, wx.Panel,
# wx.StaticText, wx.Button, and a wx.BoxSizer, but it shows the basic
# structure of any wxPython application.
#----------------------------------------------------------------------
import wx
import os 
import uuid
import time
import math
import _thread
import pathlib

import platform
import subprocess


lang='1'

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
        process = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        std_out, std_error  = process.communicate()
        lines=""
        for line in std_error.splitlines():
            lines += line.decode("utf-8")+"\n"
        return lines

def simulator_th():
      if  os_type == 'windows':
           #subprocess_cmd("cd "+base_path+"simulator & coppeliaSim.exe -s -q SampleMap.ttt")
          subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+"simulator_v4.bat")
      else:
          subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"simulator_v4.sh")


def run_client_th():

      if  os_type == 'windows':
          if lang=='2':
               subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+" run2_client_cpp.bat")
          else:
               subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+" run2_client.bat")
      else:
          if lang=='2':
              subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"run2_client_cpp.sh")
          else:
              subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"run2_client.sh")

def run_server_th():
        if  os_type == 'windows':
          subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+"run2_server.bat")
        else:
          subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"run2_server.sh")

def clear_th():
      if os_type == 'windows':
          subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+"clear.bat")
      else:
          subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"clear.sh")

def code_compile_th():
      if  os_type == 'windows':
          if lang=='2':
             if is_32:
               subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+"compile_cpp_32.bat")
             else:
              subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+"compile_cpp_64.bat")
          else:
             subprocess_cmd("cd "+base_path+"easy_setup\\"+os_type+'&'+" run2_client.bat")
      else:
         if lang=='2':
             subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"compile_cpp.sh")

         else:
              subprocess_cmd("cd "+base_path+"easy_setup/"+os_type+'; sh '+"run2_client.sh")

class MyFrame(wx.Frame):
    file_name_var=""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title,
                          pos=(150, 150), size=(250, 400))

        # Create the menubar
        menuBar = wx.MenuBar()

        # and a menu 
        menu = wx.Menu()

        # add an item to the menu, using \tKeyName automatically
        # creates an accelerator, the third param is some help text
        # that will show up in the statusbar
        menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Exit this simple sample")

        # bind the menu event to an event handler
        self.Bind(wx.EVT_MENU, self.OnTimeToClose, id=wx.ID_EXIT)

        # and put the menu on the menubar
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

        self.CreateStatusBar()

        # Now create the Panel to put the other controls on.
        panel = wx.Panel(self)

        # and a few controls
        text = wx.StaticText(panel, -1, "")
        text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        text.SetSize(text.GetBestSize())
        btn_p = wx.RadioButton(panel, 1, "Python")
        btn_c = wx.RadioButton(panel, 2, "C/C++")

        btn0 = wx.Button(panel, -1, "Choose file")
        btn00 = wx.Button(panel, -1, "Upload")
        btn1 = wx.Button(panel, -1, "Open Simulator")
        btn2 = wx.Button(panel, -1, "Compile")
        btn3 = wx.Button(panel, -1, "Clear")
        btn4 = wx.Button(panel, -1, "Run client")
        btn5 = wx.Button(panel, -1, "Run server")
        self.openFileDialog = wx.FileDialog(panel, "Open", "", "", "Python files (*.py)|*.py|(*.cc)|*.cc", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        #bind the button events to handlers
        self.Bind(wx.EVT_BUTTON, self.open_f, btn0)
        self.Bind(wx.EVT_BUTTON, self.upload, btn00)
        self.Bind(wx.EVT_RADIOBUTTON, self.choose_pl)
        self.Bind(wx.EVT_BUTTON, self.simulator, btn1)
        self.Bind(wx.EVT_BUTTON, self.code_compile, btn2)
        self.Bind(wx.EVT_BUTTON, self.clear, btn3)
        self.Bind(wx.EVT_BUTTON, self.run_client, btn4)
        self.Bind(wx.EVT_BUTTON, self.run_server, btn5)

        # Use a sizer to layout the controls, stacked vertically and with
        # a 10 pixel border around each
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(btn_p, 0, wx.ALL, 10)
        sizer.Add(btn_c, 0, wx.ALL, 10)
        sizer.Add(btn0, 0, wx.ALL, 10)
        sizer.Add(btn00, 0, wx.ALL, 10)
        sizer.Add(btn1, 0, wx.ALL, 10)
        sizer.Add(btn2, 0, wx.ALL, 10)
        sizer.Add(btn3, 0, wx.ALL, 10)
        sizer.Add(btn4, 0, wx.ALL, 10)
        sizer.Add(btn5, 0, wx.ALL, 10)

        panel.SetSizer(sizer)
        panel.Layout()

    def open_f(self,evt):
          self.openFileDialog.ShowModal()
          print(self.openFileDialog.GetPath())
          self.file_name_var=self.openFileDialog.GetPath()
          # self.openFileDialog.Destroy()
    # def OnTimeToClose(self, evt):
    #     """Event handler for the button click."""
    #     print ("See ya later!")
    #     self.Close()

    def onRadioBox(self,e): 
      print(self.rbox.GetStringSelection(),' is clicked from Radio Box' )
    
    def choose_pl(self,evt):
      global lang
      rb = evt.GetEventObject() 
      if(rb.GetLabel() == "Python"):
        lang='1'
      else:
        lang='2'


    def simulator(self,evt):
      try:
        _thread.start_new_thread( simulator_th, ( ) )

      except Exception as e:
        print(e)
        return



    def run_client(self,evt):
      try:
        _thread.start_new_thread( run_client_th, ( ) )

      except Exception as e:
        print(e)
        return





    def run_server(self,evt):
      try:
        _thread.start_new_thread( run_server_th, ( ) )

      except Exception as e:
        print(e)




    def clear(self,evt):
      try:
        _thread.start_new_thread( clear_th, ( ) )

      except Exception as e:
        print(e)



    def code_compile(self,evt):
      try:
        _thread.start_new_thread( code_compile_th, ( ) )

      except Exception as e:
        print(e)

    def choose(self,evt):
        text = wx.StaticText(panel, -1, "")
        self.file_name_var=""
        
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
        
        self.file_name_var=address
        txt.insert(0,address)


    def copy_file(self,destination,f1):
        f = open(destination, 'wb')
        data=bytearray(f1.read())
        f.write(data)
        f.close()


    def upload(self,evt):
     print("Uploading ....");
     print(lang)
     try:
        f1=open(str(self.file_name_var), 'rb')
        if lang=='2':
            destination = base_path + 'client/cpp/'
            self.copy_file(destination+"player.cc",f1)
            #self.copy_file(destination+"player_win.cc",f1)
        else:
            destination = base_path + 'client/python/player.py'
            self.copy_file(destination,f1)

        f1.close()

        print("Code is uploaded successfully!")
     except Exception as e:
        print(str(e))
        return


    # def upload(self,evt):
    #   try:
    #     _thread.start_new_thread( show_progress, ( ) )

    #   except Exception as e:
    #     print(e)
    #   return

   
    def OnFunButton(self, evt):
        """Event handler for the button click."""
        print ("Having fun yet?")

    def OnTimeToClose(self, evt):
        """Event handler for the button click."""
        print ("See ya later!")
        self.Close()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "Simple wxPython App")
        self.SetTopWindow(frame)


        frame.Show(True)
        return True
app = MyApp(redirect=True)
app.MainLoop()
