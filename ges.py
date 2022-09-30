import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
gesture=''
def get_bbox_coordinates(handLadmark, image_shape):
    """ 
    Get bounding box coordinates for a hand landmark.
    Args:
        handLadmark: A HandLandmark object.
        image_shape: A tuple of the form (height, width).
    Returns:
        A tuple of the form (xmin, ymin, xmax, ymax).
    """
    all_x, all_y = [], [] # store all x and y points in list
    for hnd in mp_hands.HandLandmark:
        all_x.append(int(handLadmark.landmark[hnd].x * image_shape[1])) # multiply x by image width
        all_y.append(int(handLadmark.landmark[hnd].y * image_shape[0])) # multiply y by image height

    return min(all_x), min(all_y), max(all_x), max(all_y)
def fing(results):
    global image,gesture
    if results.multi_hand_landmarks:
        for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
            mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS)
            # print(hand_no)
            index1=1
            index2=1
            middle1=1
            middle2=1
            ring1=1
            ring2=1
            pinky1=1
            pinky2=1
            thumb1=0
            thumb2=1
            global number1
            if (hand_landmarks.landmark[mp_hands.HandLandmark(8).value].y * image_width>=hand_landmarks.landmark[mp_hands.HandLandmark(6).value].y * image_width):
                index2=0
            if (hand_landmarks.landmark[mp_hands.HandLandmark(8).value].x * image_height>=hand_landmarks.landmark[mp_hands.HandLandmark(6).value].x * image_height):
                index1=0
            if (hand_landmarks.landmark[mp_hands.HandLandmark(12).value].y * image_width>=hand_landmarks.landmark[mp_hands.HandLandmark(10).value].y * image_width):
                middle2=0
            if (hand_landmarks.landmark[mp_hands.HandLandmark(12).value].x * image_height>=hand_landmarks.landmark[mp_hands.HandLandmark(10).value].x * image_height):
                middle1=0
            if (hand_landmarks.landmark[mp_hands.HandLandmark(16).value].x * image_height>=hand_landmarks.landmark[mp_hands.HandLandmark(14).value].x * image_height):
                ring1=0
            if (hand_landmarks.landmark[mp_hands.HandLandmark(16).value].y * image_width>=hand_landmarks.landmark[mp_hands.HandLandmark(14).value].y * image_width):
                ring2=0
            if (hand_landmarks.landmark[mp_hands.HandLandmark(20).value].x * image_height>=hand_landmarks.landmark[mp_hands.HandLandmark(18).value].x * image_height):
                pinky1=0
            if (hand_landmarks.landmark[mp_hands.HandLandmark(20).value].y * image_width>=hand_landmarks.landmark[mp_hands.HandLandmark(18).value].y * image_width):
                pinky2=0
            if (hand_landmarks.landmark[mp_hands.HandLandmark(4).value].x * image_width>=hand_landmarks.landmark[mp_hands.HandLandmark(2).value].x * image_width):
                thumb1=1
            if (hand_landmarks.landmark[mp_hands.HandLandmark(4).value].y * image_height>=hand_landmarks.landmark[mp_hands.HandLandmark(2).value].y * image_height):
                thumb2=1
            if hand_no==0:
                lef_rig=results.multi_handedness[0].classification[0].label
            elif(hand_no==1):
                lef_rig="Right" or "Left"
            # print(lef_rig)
            if (lef_rig=="Left"):
                m=[thumb1,index2,middle2,ring2,pinky2] 
                if (m==[1,1,1,1,1]):
                    gesture="HI"
                if(m==[0,1,0,0,0]):
                    gesture="ONE"
                if(m==[0,1,1,0,0]):
                    gesture="TWO"
                if(m==[0,1,1,1,0]):
                    gesture="THREE"
                if(m==[0,1,1,1,1]):
                    gesture="FOUR"
                if(m==[0,0,0,0,0]):
                    gesture="PUNCH"
                if(m==[0,0,0,0,1]):
                    gesture="WANNA PEE"
                if(m==[0,0,1,0,0]):
                    gesture="NO TOXICITY"
                if(m==[0,1,0,0,1]):
                    gesture="YO BRO"
                if(m==[1,1,0,0,1]):
                    gesture="ROCK AND ROLL"
                coords=get_bbox_coordinates(hand_landmarks,[image_height,image_width])
                cv2.rectangle(image, (coords[0]+5,coords[1]+5), (coords[2]+5,coords[3]+5), (0,255,0), 2)
                # cv2.rectangle(image, (coords[0],coords[2]+20), (coords[1],coords[2]), (0,255,0), 2)
                # gesture=""
                cv2.putText(image, gesture, (coords[0],coords[3]+25), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 2) 
        if (lef_rig=="Right"):
                m=[thumb1,index2,middle2,ring2,pinky2] 
                if (m==[0,1,1,1,1]):
                    gesture="HI"
                if(m==[1,1,0,0,0]):
                    gesture="ONE"
                if(m==[1,1,1,0,0]):
                    gesture="TWO"
                if(m==[1,1,1,1,0]):
                    gesture="THREE"
                if(m==[1,1,1,1,1]):
                    gesture="FOUR"
                if(m==[1,0,0,0,0]):
                    gesture="PUNCH"
                if(m==[1,0,0,0,1]):
                    gesture="WANNA PEE"
                if(m==[1,0,1,0,0]):
                    gesture="NO TOXICITY"
                if(m==[1,1,0,0,1]):
                    gesture="YO BRO"
                if(m==[0,1,0,0,1]):
                    gesture="ROCK AND ROLL"
                coords=get_bbox_coordinates(hand_landmarks,[image_height,image_width])
                cv2.rectangle(image, (coords[0]+5,coords[1]+5), (coords[2]+5,coords[3]+5), (0,255,0), 2)
                # cv2.rectangle(image, (coords[0],coords[2]+20), (coords[1],coords[2]), (0,255,0), 2)
                # gesture=""
                cv2.putText(image, gesture, (coords[0],coords[3]+30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 2) 
    
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=1
    ) as hands:
  while cap.isOpened():
    gesture=""
    imgBG=cv2.imread(r'F:\Ojas SSD\Ojas\Python\Opencv\Resources\BG.png')
    numberim=cv2.imread(r'F:\Ojas SSD\Ojas\Python\Opencv\Gesture\Waiting.png')
    success, image = cap.read()
    image_height, image_width, _ = image.shape
    # print(image_height)
    # print(image_width)
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image_height, image_width, _ = image.shape
    results=hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # image=cv2.flip(image,1)
    m=fing(results)
    # print(m)
    # for rect in results.hand_rects:
    #     print(rect)
    image=cv2.resize(image,(0,0),None,2.5,1.875)
    cv2.imshow("Gesture",image)
    key = cv2.waitKey(1)
    # if cv2.waitKey(5) & 0xFF == 27:
    #   break
    if key == ord('s'):
        quit()
cap.release()