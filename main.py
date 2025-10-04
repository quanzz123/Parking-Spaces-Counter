import  cv2
import cvzone
import pickle
import numpy as np

width, height = 107, 48
cap = cv2.VideoCapture('E:\\WORKSPACE\\CV\\ParkingSpaces\\carPark.mp4')

with open('carParkPos', 'rb') as f:
    posList = pickle.load(f)
def checkParkingSpace(imgPro, img):
    spaceCounter = 0
    imgwidth, imgheight = img.shape[:2]
    for pos in posList:
        x, y =pos
        imgCrop = imgPro[y:y+height, x:x+width]
        # cv2.imshow(str(x*y), imgCrop)
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0,255,0)
            thickness = 4
            spaceCounter += 1
        else:
            color = (0,0,255)
            thickness = 2
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height),color, thickness)
        cv2.putText(img, str(count), (x, y + height - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
    cv2.putText(img, f'CHO TRONG: {spaceCounter}/{len(posList)}', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3 )

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    ret, frame = cap.read()
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255,
                                         cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV,
                                         25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDialate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDialate, frame)
    # for pos in posList:
    #     cv2.rectangle(frame,pos,(pos[0] + width,pos[1] + height),(255,0,255),2)
    cv2.imshow('frame', frame)
    # cv2.imshow('imgage Blur', imgThreshold)
    # cv2.imshow('imgage Median', imgMedian)
    # cv2.imshow('imgage Dialate', imgDialate)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()