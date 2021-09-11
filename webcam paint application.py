
import cv2
import numpy as np
from collection import deque 
#defined upper and lower boundaries for a colour to be considered"blue"
blueLower=np.array([100,60,60])
blueUpper=np.array([140,255,255])
#define 5*5 kernel errosion and dillution(this removes video and displays only the line)
kernel=np.one((5,5),np.unit8)
#setup deques to store separate colour in separate arrays
bPoint=[deque(maxlen=512)]
rPoint=[deque(maxlen=512)]
yPoint=[deque(maxlen=512)]
gPoint=[deque(maxlen=512)]
bindex=0
rindex=0
yindex=0
gindex=0
colors=[(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
colorindex=0
#setup the paint interface
paintwindow=np.zeros((471,636,3))+255
paintwindow=cv2.rectangle(paintwindow,(40,1),(140,65),(0,0,0),2)