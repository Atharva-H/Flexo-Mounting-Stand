import cv2 

vid = cv2.VideoCapture(0)
vid2 = cv2.VideoCapture(1)

cam_x = 640
cam_y = 480

while(True): 
    ret, frame1 = vid.read()  
    ret, frame2 = vid2.read()  
    frame1 = cv2.line(frame1, (int(cam_x/2),0),(int(cam_x/2),cam_y), (0, 255, 0) , 3) 
    frame1 = cv2.line(frame1, (0,int(cam_y/2)),(cam_x,int(cam_y/2)), (0, 255, 0) , 3)
    frame2 = cv2.line(frame2, (int(cam_x/2),0),(int(cam_x/2),cam_y), (0, 255, 0) , 3) 
    frame2 = cv2.line(frame2, (0,int(cam_y/2)),(cam_x,int(cam_y/2)), (0, 255, 0) , 3)
    
    fm1C = frame1[int(cam_y/2):int(cam_y/2)+int(cam_y/4),int(cam_x/2):int(cam_x/2)+int(cam_x/4)]

    fm1S = cv2.resize(fm1C, (cam_x, cam_y)) 
    
    fm1 = cv2.imshow('Cam_01', fm1S)  
    fm2 = cv2.imshow('Cam_02', frame1)  

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
   
vid.release() 
vid2.release()  
cv2.destroyAllWindows() 