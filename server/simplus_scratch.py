#pip install bottle

from bottle import route, run, template,request,response
import robotApi

server_ip='127.0.0.1'
server_port=19999
print("Please type in server ip address in the following format => 127.0.0.1")
server_ip= input()
print("Please type in server port in the following format => 19999")
server_port= input()
vapi=robotApi.VrepApi(server_ip=server_ip,server_port=int(server_port),waitUntilConnected=True,doNotReconnectOnceDisconnected=True,timeOutInMs=5000,commThreadCycleInMs=5)
rapi=vapi.init_robotApi(trapConfig=None,robot_base='ePuck_base',robot_namespace="ePuck_",robot_motors={"left":'leftJoint',"right":'rightJoint',"radius":0.02},proximity_sensor={"num":8,"name":'proxSensor'},camera={"name":'camera',"joint":None},color_sensor={"num":1,"name":'lightSensor'},gps_enabled=True)
sapi=vapi.init_serverApi(serverConfig=r'serverconfig.txt')

@route('/set_wheels')
def set_wheels():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers["Set-Cookie"]= 'SameSite=None;Secure'
	rw=request.GET.get('rw', '').strip()
	lw=request.GET.get('lw', '').strip()
	rapi.setJointSpeed(right_rotation=float(rw),left_rotation=float(lw))
	print("set_wheels")
	return "set_wheels"


@route('/set_led')
def set_led():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers["Set-Cookie"]= 'SameSite=None;Secure'
	status=request.GET.get('status', '').strip()
	if status == "off":
		rapi.setLED("off")
	elif status == "blue":
		rapi.setLED("blue")
	elif status == "green":
		rapi.setLED("green")
	elif status == "red":
		rapi.setLED("red")

	return "set_led"


@route('/get_proximity')
def get_proximity():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers["Set-Cookie"]= 'SameSite=None;Secure'
	number=request.GET.get('number', '').strip()
	print(number)
	proximity=rapi.getProximitySensor(int(number))
	value=100000
	if(proximity[0]==True):
		value=proximity[1]
	return str(value);


@route('/get_color')
def get_color():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers["Set-Cookie"]= 'SameSite=None;Secure'
	sensor=request.GET.get('sensor', '').strip()
	color='red'; # blue,green,gray,black
	rgb=[0,0,0]
	if sensor == "center":
		rgb=rapi.getColorSensor(0)
	elif sensor == "right":
		rgb=rapi.getColorSensor(2)
	elif sensor == "left":
		rgb=rapi.getColorSensor(1)

	if(rgb[0]>rgb[1]):
		color='red'
	elif(rgb[1]>rgb[2]):
		color='green'
	else:
		color='blue'

	return color



@route('/get_position')
def get_position():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers["Set-Cookie"]= 'SameSite=None;Secure'
	position=request.GET.get('position', '').strip()
	value=0;
	pose=rapi.getRobotPose()
	if position == "x":
		value=pose[0]
	elif position == "y":
		value=pose[1]
	elif position == "z":
		value=pose[2]

	return str(value);


@route('/get_orientation')
def get_orientation():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers["Set-Cookie"]= 'SameSite=None;Secure'
	orientation=request.GET.get('orientation', '').strip()
	value=0;
	pose=rapi.getRobotPose()
	if orientation == "Ro":
		value=pose[3]
	elif orientation == "Phi":
		value=pose[4]

	elif orientation == "Theta":
		value=pose[5]

	return str(value);


@route('/get_distance_victim')
def get_distance_victim():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers["Set-Cookie"]= 'SameSite=None;Secure'
	print("get_distance_victim");
	value=1;

	pose=rapi.getRobotXYZ()
	print(pose)
	res=-1
	res=sapi.callAction("find_victim",pose[0],pose[1],pose[2])
	if(res>=0):
		value=0.0
	else:
		value=10
	return str(value);



@route('/get_sim_status')
def get_sim_status():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers["Set-Cookie"]= 'SameSite=None;Secure'
	print("get_sim_status");
	is_started = False
	is_started = sapi.get_status()
	value=1
	if not is_started:
		value=-1
	return str(value); #0


@route('/send_action')
def send_action():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers["Set-Cookie"]= 'SameSite=None;Secure'
	action=request.GET.get('action', '').strip()
	pose=rapi.getRobotXYZ()
	value=0
	if action == 'Find Victim':
		res=sapi.callAction("find_victim",pose[0],pose[1],pose[2])
	elif action == "Find Checkpoint":
		res=sapi.callAction("find_checkpoint",pose[0],pose[1],pose[2])
	elif action == "Rescue Victim":
		res=sapi.callAction("rescue_victim",pose[0],pose[1],pose[2])

	return str(value);




run(host='localhost', port=8080)
