# minimal code for running our program

import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture('PoseVideos/1.mp4')
pTime = 0

while True:
    success, img = cap.read()
    
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        # draw the landmarks on the video
        mpDraw.draw_landmarks(img, results.pose_landmarks,
                              mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print('landmarck id:',id)
            print(lm)
            # owe get the landmark position in pixels
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    # Draw the fps
    # cTime = time.time()
    # fps = 1/(cTime-pTime)
    # pTime = cTime

    # cv2.putText(img, str(int(fps)), (70, 50),
    #             cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    

    cv2.imshow("Image", img)
    cv2.waitKey(100)  # wait a milisecond
