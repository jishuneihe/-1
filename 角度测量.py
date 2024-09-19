import cv2
import math
path='jiaoduceliang.jpeg'
img=cv2.imread(path)
pointLsit=[]
def mousePoints(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        size=len(pointLsit)
        if size!=0 and size%3!=0:
            cv2.line(img,tuple(pointLsit[round((size-1)/3)*3]),(x,y),(0,0,255),2)

        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointLsit.append([x,y])
        print(pointLsit)
        print(x,y)
# pts1=x1,y1
# pts2=x2,y2
def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getAngle(pointList):

    pt1,pt2,pt3=pointList[-3:]
    m1=gradient(pt1,pt2)
    m2=gradient(pt1,pt3)
    angR=math.atan((m2-m1)/(1+(m2*m1)))
    angD=round(math.degrees(angR))

    cv2.putText(img,str(angD),(pt1[0]-40,pt1[1]-20),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1.5,(0,0,255),2)




while True:
    if len(pointLsit)%3==0 and len(pointLsit)!=0:
        getAngle(pointLsit)
    cv2.imshow('Image',img)
    cv2.setMouseCallback("Image",mousePoints)
    key=cv2.waitKey(1) & 0xFF

    if key==ord('q'):
        pointLsit=[]
        img=cv2.imread(path)
        # cv2.imshow("Image",img)
    elif key==ord('w'):
        cv2.destroyWindow()
        break





































































