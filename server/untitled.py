try:
    import vrep
except:
    print('--------------------------------------------------------------')
    print('"vrep.py" could not be imported. This means very probably that')
    print('either "vrep.py" or the remoteApi library could not be found.')
    print('Make sure both are in the same folder as this file,')
    print('or appropriately adjust the file "vrep.py"')
    print('--------------------------------------------------------------')
    print('')


vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', 19999, True, True,5000, 5)  # Connect to V-REP
print("client id", clientID)