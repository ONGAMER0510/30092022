import cv2
import mediapipe as mp
import time
import random
import keyboard
from threading import Thread
import tkinter as tk
from tkinter.ttk import Style
from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()
# cv2.imshow("HEY",numberim)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
runhum=0
runai=0
start=False
new_game=0
innings=0
target=0
runs=0
number1=0
choice=0
inn="Bat"
tar1=0
tar2=0
timeout=1000
timehand=1000
loop1=0
over=1000
lastrand=0
six1=1000
four1=1000
num=0
randomNumber=0
gesAI=[r"F:\Ojas SSD\Ojas\Python\Opencv\Gesture\one.png",r"F:\Ojas SSD\Ojas\Python\Opencv\Gesture\two.png",r"F:\Ojas SSD\Ojas\Python\Opencv\Gesture\three.png",r"F:\Ojas SSD\Ojas\Python\Opencv\Gesture\four.png",r"F:\Ojas SSD\Ojas\Python\Opencv\Gesture\five.png",r"F:\Ojas SSD\Ojas\Python\Opencv\Gesture\six.png",r"F:\Ojas SSD\Ojas\Python\Opencv\Gesture\seven.png",r"F:\Ojas SSD\Ojas\Python\Opencv\Gesture\eight.png",r"F:\Ojas SSD\Ojas\Python\Opencv\Gesture\nine.png",r"F:\Ojas SSD\Ojas\Python\Opencv\Gesture\ten.png",r"F:\Ojas SSD\Ojas\Python\Opencv\Gesture\eleven.png"]
def box(title,message):
    messagebox.showinfo(title,message)
def odd():
    global choice
    choice=1
def eve():
    global choice
    choice=0
def show_frame():
    global image
def number(results):
    if results.multi_hand_landmarks:
        for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
                """print(f'HAND NUMBER: {hand_no+1}')
                print('-----------------------')"""
                index=True
                middle=True
                ring=True
                pinky=True
                thumb=False
                global number1
                if (hand_landmarks.landmark[mp_hands.HandLandmark(8).value].y * image_width>=hand_landmarks.landmark[mp_hands.HandLandmark(6).value].y * image_width):
                    index=False
                if (hand_landmarks.landmark[mp_hands.HandLandmark(12).value].y * image_width>=hand_landmarks.landmark[mp_hands.HandLandmark(10).value].y * image_width):
                    middle=False
                if (hand_landmarks.landmark[mp_hands.HandLandmark(16).value].y * image_width>=hand_landmarks.landmark[mp_hands.HandLandmark(14).value].y * image_width):
                    ring=False
                if (hand_landmarks.landmark[mp_hands.HandLandmark(20).value].y * image_width>=hand_landmarks.landmark[mp_hands.HandLandmark(18).value].y * image_width):
                    pinky=False
                if (hand_landmarks.landmark[mp_hands.HandLandmark(4).value].x * image_width>=hand_landmarks.landmark[mp_hands.HandLandmark(2).value].x * image_width):
                    thumb=True
                if(index==True and middle==False and ring==False and pinky==False and thumb==False):
                    number1=1
                elif(index==True and middle==True and ring==False and pinky==False and thumb==False):
                    number1=2
                elif(index==True and middle==True and ring==True and pinky==False and thumb==False):
                    number1=3
                elif(index==True and middle==True and ring==True and pinky==True and thumb==False):
                    number1=4
                elif(index==True and middle==True and ring==True and pinky==True and thumb==True):
                    number1=5
                elif(index==False and middle==False and ring==False and pinky==False and thumb==True):
                    number1=6
                elif(index==True and middle==False and ring==False and pinky==False and thumb==True):
                    number1=7
                elif(index==True and middle==True and ring==False and pinky==False and thumb==True):
                    number1=8
                elif(index==True and middle==True and ring==True and pinky==False and thumb==True):
                    number1=9
                elif(index==True and middle==False and ring==False and pinky==True and thumb==False):
                    number1=10
                elif(index==True and middle==False and ring==False and pinky==True and thumb==True):
                    number1=11
    return number1
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    max_num_hands=1) as hands:
  while cap.isOpened():
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
    '''if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())'''
    if start:
        timer = time.time() - initialTime
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        randomNumber = random.randint(1, 11)
        num=number(results)
#             inn="Bat"
# #choose odd or eve LEFT
# #             if keyboard.read_key() == "o":
# #                 chosen=0
# #             elif keyboard.read_key() == "e":
# #                 chosen=1
# #             if(num%2==chosen):
# #choose to bowl or bat
# #                     if keyboard.read_key() == "t":
# #                         inn="Bat"
# #                     elif keyboard.read_key() == "l":
# #                         inn="Bowl"
# #             else:
# #                 #AI
# #                 inn="Bat"
#         else:
        cv2.putText(imgBG, str(int((3-timer)+1)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
        # cv2.putText(imgBG, runs, (605, 200), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
        if (int(timer)==2):
            runhum=0
            runai=0
            numberim=cv2.imread(gesAI[randomNumber-1])
            timehand=time.time()
            lastrand=numberim
            # print(f"AI:{randomNumber} Your:{num} runs:{runs}")
            start=False
            # print(f'{num} {randomNumber}')
            if inn=="Bat":
                if(num==randomNumber):
                    innings+=1
                    if(innings==2):
                        new_game=0
                        # print(f'Your runs:{tar1} AI runs:{tar2}')
                        innings=0
                        inn="Bat"
                    # print(hand_landmarks.landmark[mp_hands.HandLandmark(8).value].z * image_width)
                    else:
                        new_game=1
                    tar1=runs
                    runs=0
                    inn="Bowl"
                    timeout=time.time()
                    # print(tar1)
                else:
                    runs+=num
                runhum=runs
            else:
                if(num==randomNumber):
                    innings+=1
                    if(innings==2):
                        new_game=0
                        if(runai<=tar1):
                            inn="Bat"
                            runhum=0
                            runai=0
                            start=False
                            new_game=0
                            innings=0
                            target=0
                            runs=0
                            number1=0
                            choice=0
                            tar1=0
                            tar2=0
                            timeout=1000
                            timehand=1000
                            loop1=0
                            over=1000
                            lastrand=0
                            box("Decision", "You won against an AI")
                    else:
                        new_game=1
                    tar2=runs
                    runs=0
                    inn="Bat"
                    timeout=time.time()
                else:
                    runs+=randomNumber
                runai=runs
        # start=True
            # print(runs,innings)
    if (abs(time.time()-timeout)<3):
        cv2.putText(imgBG,"OUT", (540, 440), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4) 
    if(abs(time.time()-timehand)<2):
        numberim=cv2.imread(gesAI[randomNumber-1])
    cv2.putText(imgBG, str(runhum), (1076, 214), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 4)
    cv2.putText(imgBG, str(runai), (372, 214), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 4) 
    if(innings>0): 
        # print(tar1,tar2)
        if (inn=="Bowl"):
            cv2.putText(imgBG, "AI needs "+str(tar1-runai+1)+" runs to WIN this game", (60, 60), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 4)
        else:
            cv2.putText(imgBG, str(tar1), (372, 214), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 4) 
    # if ((num==6 and inn=="Bat") or (randomNumber==6 and inn=="Bowl")):
    #         six1=time.time()
    # elif((num==4 and inn=="Bat")or (randomNumber==4 and inn=="Bowl")):
    #     four1=time.time()
    if(runai>tar1):
        innings=0
        new_game=0
        inn="Bat"
        runhum=0
        runai=0
        start=False
        new_game=0
        innings=0
        target=0
        runs=0
        number1=0
        choice=0
        inn="Bat"
        tar1=0
        tar2=0
        timeout=1000
        timehand=1000
        loop1=0
        over=1000
        lastrand=0
        box("Decision", "AI Won Againt You")

    if(inn=="Bat"):
        cv2.putText(imgBG, "Batting", (920, 130), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 2)
        cv2.putText(imgBG, "Bowling", (196, 130), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 2)
    elif(inn=="Bowl"):
        cv2.putText(imgBG, "Bowling", (920, 130), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 2)
        cv2.putText(imgBG, "Batting", (196, 130), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 2)
    if(abs(time.time()-six1)<2):
        cv2.putText(imgBG, "Six", (540, 440), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 4)
    if(abs(time.time()-four1)<2):
        cv2.putText(imgBG, "Four", (540, 440), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 4)
    # Flip the image horizontally for a selfie-view display.
    imageScaled=cv2.resize(image,(0,0),None,0.875,0.875)
    numsca=cv2.resize(numberim,(0,0),None,0.875,0.875)
    imageScaled=imageScaled[:,80:480]
    imageh,imagew,_=imageScaled.shape
    # print(imageh)
    # print(imagew)
    imgBG[234:654,795:1195]=cv2.flip(imageScaled, 1)
    imgBG[234:654,92:492]=numberim
    imgBG=cv2.resize(imgBG,(0,0),None,1.25,1.25)
    cv2.imshow("BG",imgBG)
    # cv2.imshow("B",numberim)
    # cv2.imshow("B",numsca)
    # numberim[:, :, [0, 2]] = numberim[:, :, [2, 0]]
    # cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    # cv2.imshow('Scaled', cv2.flip(imageScaled, 1))
    key = cv2.waitKey(1)
    # if cv2.waitKey(5) & 0xFF == 27:
    #   break
    
    if key == ord('s'):
        initialTime = time.time()
        start=True
        if new_game!=1:
            new_game=0

cap.release()