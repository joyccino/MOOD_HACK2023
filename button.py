import cv2
import numpy as np 

# button dimensions (y1,y2,x1,x2)
button = [20,60,50,250]

# function that handles the mousclicks
def process_click(event, x, y,flags, params):
    # check if the click is within the dimensions of the button
    if event == cv2.EVENT_LBUTTONDOWN:
        if y > button[0] and y < button[1] and x > button[2] and x < button[3]:   
            print('Clicked on Button!')

# function that handles the trackbar
def startCapture(val):
    # check if the value of the slider 
    if val == 1:
        print('Capture started!')
    else:
        print('Capture stopped!')            

# create a window and attach a mousecallback and a trackbar
cv2.namedWindow('Control')
cv2.setMouseCallback('Control',process_click)
cv2.createTrackbar("Capture", 'Control', 0,1, startCapture)

# create button image
control_image = np.zeros((80,300), np.uint8)
control_image[button[0]:button[1],button[2]:button[3]] = 180
cv2.putText(control_image, 'Button',(100,50),cv2.FONT_HERSHEY_PLAIN, 2,(0),3)

#show 'control panel'
cv2.imshow('Control', control_image)
cv2.waitKey(0)
cv2.destroyAllWindows()