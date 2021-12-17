import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mphand =mp.solutions.hands
#偵測手
hands = mphand.Hands() 
#畫上手座標
mpDraw = mp.solutions.drawing_utils
#改變點顏色粗度
handlmsSy =  mpDraw.DrawingSpec(color=(0,0,255),thickness=5)
#改變線顏色粗度
handconSy = mpDraw.DrawingSpec(color=(0,255,0),thickness=10)
pTime = 0
CTime = 0

while True:
    ret, img = cap.read()
    if ret:
        #BGR轉RGB
        imgRGN = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGN)
        #回傳手21個座標
        #print(result.multi_hand_landmarks)
        #改變視窗大小
        imgHeight = img.shape[0]
        imgWidth = img.shape[1]
        #判斷偵測到手
        if result.multi_hand_landmarks:
            for handlms in result.multi_hand_landmarks:
                #mpDraw.draw_landmarks(圖,手的點,連結點,點顏色、粗度,線顏色、粗度)
                mpDraw.draw_landmarks(img,handlms,mphand.HAND_CONNECTIONS,
                handlmsSy,handconSy)
                #把21個點座標顯示出來
                for i, lm in enumerate(handlms.landmark):
                    #改成圖片座標
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)
                    #顯示點是第幾個點
                    #cv2.putText(圖,轉換成字串,(位置),文字,大小,顏色,粗度)
                    cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),2)
                    
                    #特別放大某個點
                    # if i == 4:
                    #     cv2.circle(img,(xPos,yPos),10,(0,0,255),cv2.FILLED)

         
                    print(i, xPos,yPos)
        
        #顯示FPS
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img,f"FPS:{int(fps)}",(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
        cv2.imshow('img',img)

    if cv2.waitKey(2) == ord('q'):
        break