

import cv2
import numpy
import matplotlib.pyplot as plt
import matplotlib.patches as patches

################################
##  RCJRVision
################################
# One of the best modules that been desinged and used in many robocup competition.
# It is now specially tuned for RoboCup Rescue Simulatiuon
# you can detect all letters and signs with three simple step
from RCJRVision import RCJRVision  # Import module


img = cv2.imread('img/vision.png')  # Read image file
print("Vision image size: ", img.shape) #(860, 1321, 3)
my_vision = RCJRVision.HSUVision()  # Instantiate
letter, center = my_vision.find_HSU(img)  # Call the function

print(center) # [269.5, 802.5]
print(letter)
center_x = int(center[0])
center_y = int(center[1])

### Making Borders aroud detected victim

border_size=10

# img = cv2.rectangle(img, (center_x-border_size,center_y-border_size), (center_x+border_size,center_y+border_size), color=(255, 0, 0), thickness=4) 
plt.subplot(111), plt.imshow(img, cmap='gray'), plt.title('Victim')  # Plot the Image
plt.show()  # Show the plotter window (You should see the image in a new window now)



################################
##  GRPC 
################################
# Actually, You don't need this part for development, only for those who are more interested
# As you may know all programs for this leagues are communicating via network.
# For this communication we need to standardize some protocol and messaging system
# It has been done with low-latency and performance in mind so we choose GRPC
# The best practice for this modules are **client.py** and **server.py** in this project.