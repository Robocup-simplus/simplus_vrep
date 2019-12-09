#pip install bottle

from bottle import Bottle,response,request
import threading
# print("Please type in server ip address in the following format => 127.0.0.1")
# server_ip= input()
# print("Please type in server port in the following format => 19999")
# server_port= input()
class ScratchApi(Bottle):
        def __init__(self,vapi,rapi,sapi,host='localhost', port=8080):
            super(ScratchApi, self).__init__()
            self.rapi=rapi
            self.vapi=vapi
            self.sapi=sapi
            self.route('/set_wheels', callback=self.set_wheels)
            self.route('/set_led', callback=self.set_led)
            self.route('/get_color', callback=self.get_color)
            self.route('/get_position', callback=self.get_position)
            self.route('/get_orientation', callback=self.get_orientation)
            self.route('/get_distance_victim', callback=self.get_distance_victim)
            self.route('/get_sim_status', callback=self.get_sim_status)
            self.route('/send_action', callback=self.send_action)
            self.run(host=host, port=port)

        def set_wheels(self):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.headers["Set-Cookie"]= 'SameSite=None;Secure'
            rw=request.GET.get('rw', '').strip()
            lw=request.GET.get('lw', '').strip()
            self.rapi.setJointSpeed(right_rotation=float(rw),left_rotation=float(lw))
        #     print("set_wheels")
            return "set_wheels"


        def set_led(self):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.headers["Set-Cookie"]= 'SameSite=None;Secure'
            status=request.GET.get('status', '').strip()
            if status == "off":
                self.rapi.setLED("off")
            elif status == "blue":
                self.rapi.setLED("blue")
            elif status == "green":
                self.rapi.setLED("green")
            elif status == "red":
                self.rapi.setLED("red")

            return "set_led"


        def get_proximity(self):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.headers["Set-Cookie"]= 'SameSite=None;Secure'
            number=request.GET.get('number', '').strip()
        #     print(number)
            proximity=self.rapi.getProximitySensor(int(number))
            value=100000
            if(proximity[0]==True):
                value=proximity[1]
            return str(value);


        def get_color(self):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.headers["Set-Cookie"]= 'SameSite=None;Secure'
            sensor=request.GET.get('sensor', '').strip()
            color='red'; # blue,green,gray,black
            rgb=[0,0,0]
            if sensor == "center":
                rgb=self.rapi.getColorSensor(0)
            elif sensor == "right":
                rgb=self.rapi.getColorSensor(2)
            elif sensor == "left":
                rgb=self.rapi.getColorSensor(1)
            if(rgb[0]<10 and rgb[1]<10 and rgb[2]<10):
                color='black'
            elif(abs(rgb[0]-rgb[1])<15 and abs(rgb[2]-rgb[1])<15 and abs(rgb[0]-rgb[2])<15 ):
                color='grey'
            elif(rgb[0]>rgb[1]):
                color='red'
            elif(rgb[1]>rgb[2]):
                color='green'
            else:
                color='blue'

            return color



        def get_position(self):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.headers["Set-Cookie"]= 'SameSite=None;Secure'
            position=request.GET.get('position', '').strip()
            value=0;
            pose=self.rapi.getRobotPose()
            if position == "x":
                value=pose[0]
            elif position == "y":
                value=pose[1]
            elif position == "z":
                value=pose[2]

            return str(value);


        def get_orientation(self):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.headers["Set-Cookie"]= 'SameSite=None;Secure'
            orientation=request.GET.get('orientation', '').strip()
            value=0;
            pose=self.rapi.getRobotPose()
            if orientation == "Ro":
                value=pose[3]
            elif orientation == "Phi":
                value=pose[4]

            elif orientation == "Theta":
                value=pose[5]

            return str(value);


        def get_distance_victim(self):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.headers["Set-Cookie"]= 'SameSite=None;Secure'
        #     print("get_distance_victim");
            value=1;

            pose=self.rapi.getRobotXYZ()
            print(pose)
            res=-1
            res=self.sapi.callAction("find_victim",pose[0],pose[1],pose[2])
            if(res>=0):
                value=0.0
            else:
                value=10
            return str(value);



        def get_sim_status(self):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.headers["Set-Cookie"]= 'SameSite=None;Secure'
            print("get_sim_status");
            is_started = False
            is_started = self.sapi.get_status()
            value=1
            if not is_started:
                value=-1
        #     print(value)
            return str(value); #0


        def send_action(self):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.headers["Set-Cookie"]= 'SameSite=None;Secure'
            action=request.GET.get('action', '').strip()
            pose=self.rapi.getRobotXYZ()
            value=0
            if action == 'Find Victim':
                res=self.sapi.callAction("find_victim",pose[0],pose[1],pose[2])
            elif action == "Find Checkpoint":
                res=self.sapi.callAction("find_checkpoint",pose[0],pose[1],pose[2])
            elif action == "Rescue Victim":
                res=self.sapi.callAction("rescue_victim",pose[0],pose[1],pose[2])
            else:
                res=self.sapi.callAction(action,pose[0],pose[1],pose[2])
            return str(value);


#scratch
class ScratchThread(threading.Thread):
    def __init__(self,vapi,rapi,sapi):
        threading.Thread.__init__(self)
        self.vapi=vapi
        self.rapi=rapi
        self.sapi=sapi
    def run(self):
        sc=ScratchApi(self.vapi,self.rapi,self.sapi)
#endscratch