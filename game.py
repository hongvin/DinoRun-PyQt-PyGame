__author__   = "Koay Hong Vin"
__MatricNo__ = "KIE160111"
__Title__    = "Assignment 2"
__GitHub__   = "https://github.com/khvmaths"

import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton

import cv2
import numpy as np 
import math
import pygame
import random
import os
import time

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-300,-300)

from collections import deque
import argparse
#import gamegui

"""GUI"""
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 317)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(640, 10, 251, 301))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 141, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 40, 221, 151))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 260, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 210, 141, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 121, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 220, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 621, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 601, 151))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 220, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 290, 171, 16))
        self.label_9.setObjectName("label_9")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(160, 210, 141, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 121, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 290, 291, 20))
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dino Run"))
        self.groupBox.setTitle(_translate("Dialog", "OpenCV Processing"))
        self.label.setText(_translate("Dialog", "Original Image"))
        self.label_4.setText(_translate("Dialog", "Processed Information"))
        self.pushButton_5.setText(_translate("Dialog", "Stop CV"))
        self.groupBox_3.setTitle(_translate("Dialog", "Score Board"))
        self.pushButton_3.setText(_translate("Dialog", "Normal Start"))
        self.groupBox_2.setTitle(_translate("Dialog", "Game Area"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_4.setText(_translate("Dialog", "Start with CV"))
        self.label_9.setText(_translate("Dialog", "TextLabel"))
        self.groupBox_4.setTitle(_translate("Dialog", "High Score"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:7pt;\">Developed by </span><span style=\" font-size:9pt; font-weight:600;\">Koay Hong Vin (KIE160111)</span></p></body></html>"))


"""THE CV IS HIGHLY DEPENDENT ON ENVIRONMENT/NOISE"""
threshold = 60  #  BINARY threshold
blurValue = 41  # GaussianBlur parameter
Lower_bound=np.array([110,50,50])
Upper_bound=np.array([130,255,255])
pts=deque(maxlen=64)

"""OPENCV PART == TODO: Change the whole idea of detecting movement"""
class FrameThread(QThread,Ui_Dialog):
    imgLab = None
    device = None

    def __init__(self,deviceIndex,imgLab,action):
        QThread.__init__(self)
        self.imgLab = imgLab
        self.action=action
        self.deviceIndex = deviceIndex

        self.device = cv2.VideoCapture(self.deviceIndex)  
        self.device.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
        self.device.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)

    def run(self):
        if self.device.isOpened():
            last_center=(0,0)
            try:
                while True:
                    ret, frame = self.device.read()
                    height, width, bytesPerComponent = frame.shape
                    bytesPerLine = bytesPerComponent * width
                    
                    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)

                        
                    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
                    kernel=np.ones((5,5),np.uint8)
                    mask=cv2.inRange(hsv,Lower_bound,Upper_bound)
                    mask=cv2.erode(mask,kernel,iterations=2)
                    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
                    mask=cv2.dilate(mask,kernel,iterations=1)
                    res=cv2.bitwise_and(frame,frame,mask=mask)
                    cnts,heir=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]
                    center=None

                    if len(cnts)>0:
                        c=max(cnts,key=cv2.contourArea)
                        ((x,y),radius)=cv2.minEnclosingCircle(c)
                        M=cv2.moments(c)
                        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
                        print(center)

                        if radius>5:
                            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
                            cv2.circle(frame,center,5,(0,0,255),-1)
                    pts.appendleft(center)

                    for i in range(1,len(pts)):
                        if pts[i-1] is None or pts[i] is None:
                            continue
                        thick=int(np.sqrt(len(pts)/float(i+1))*2.5)
                        cv2.line(frame,pts[i-1],pts[i],(0,0,255),thick)
                    
                    flipped=cv2.flip(frame,1)
                    image = QImage(flipped, width, height, bytesPerLine, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(image)
                    pixmap = pixmap.scaled(221, 191, QtCore.Qt.KeepAspectRatio)

                    if (center==None):
                        continue
                    else:
                        if(abs(center[0]-last_center[0])>5 and abs(center[1]-last_center[1]<20)):
                            if(center[0]>last_center[0]):
                                pass
                            else:
                                pass
                        elif(abs(center[1]-last_center[1]))>10:
                            if(center[1]>last_center[1]):
                                act='Down'
                            else:
                                act='Up'
                        else:
                            act='No action'
                    last_center=center

                    self.imgLab.setPixmap(pixmap)
                    self.action.setText(act)
            except:
                pass


    
    def destoryed(self,QObject=None):
        self.device.release()


"""MAIN GAME TRESHOLD"""
pygame.init()

scr_size = (width,height) = (600,150)
FPS = 60
gravity = 0.6

black = (0,0,0)
white = (255,255,255)
background_col = (235,235,235)

high_score = 0

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Run ")

jump_sound = pygame.mixer.Sound('sprites/jump.wav')
die_sound = pygame.mixer.Sound('sprites/die.wav')
checkPoint_sound = pygame.mixer.Sound('sprites/checkPoint.wav')

def load_image(
    name,
    sizex=-1,
    sizey=-1,
    colorkey=None,
    ):

    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)

    if sizex != -1 or sizey != -1:
        image = pygame.transform.scale(image, (sizex, sizey))

    return (image, image.get_rect())

def load_sprite_sheet(
        sheetname,
        nx,
        ny,
        scalex = -1,
        scaley = -1,
        colorkey = None,
        ):
    fullname = os.path.join('sprites',sheetname)
    sheet = pygame.image.load(fullname)
    sheet = sheet.convert()

    sheet_rect = sheet.get_rect()

    sprites = []

    sizex = sheet_rect.width/nx
    sizey = sheet_rect.height/ny

    for i in range(0,ny):
        for j in range(0,nx):
            rect = pygame.Rect((j*sizex,i*sizey,sizex,sizey))
            image = pygame.Surface(rect.size)
            image = image.convert()
            image.blit(sheet,(0,0),rect)

            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey,pygame.RLEACCEL)

            if scalex != -1 or scaley != -1:
                image = pygame.transform.scale(image,(scalex,scaley))

            sprites.append(image)

    sprite_rect = sprites[0].get_rect()

    return sprites,sprite_rect

def disp_gameOver_msg(retbutton_image,gameover_image):
    retbutton_rect = retbutton_image.get_rect()
    retbutton_rect.centerx = width / 2
    retbutton_rect.top = height*0.52

    gameover_rect = gameover_image.get_rect()
    gameover_rect.centerx = width / 2
    gameover_rect.centery = height*0.35

    screen.blit(retbutton_image, retbutton_rect)
    screen.blit(gameover_image, gameover_rect)

def extractDigits(number):
    if number > -1:
        digits = []
        i = 0
        while(number/10 != 0):
            digits.append(number%10)
            number = int(number/10)

        digits.append(number%10)
        for i in range(len(digits),5):
            digits.append(0)
        digits.reverse()
        return digits

class Dino():
    def __init__(self,sizex=-1,sizey=-1):
        self.images,self.rect = load_sprite_sheet('dino.png',5,1,sizex,sizey,-1)
        self.images1,self.rect1 = load_sprite_sheet('dino_ducking.png',2,1,59,sizey,-1)
        self.rect.bottom = int(0.98*height)
        self.rect.left = width/15
        self.image = self.images[0]
        self.index = 0
        self.counter = 0
        self.score = 0
        self.isJumping = False
        self.isDead = False
        self.isDucking = False
        self.isBlinking = False
        self.movement = [0,0]
        self.jumpSpeed = 11.5

        self.stand_pos_width = self.rect.width
        self.duck_pos_width = self.rect1.width

    def draw(self):
        screen.blit(self.image,self.rect)

    def checkbounds(self):
        if self.rect.bottom > int(0.98*height):
            self.rect.bottom = int(0.98*height)
            self.isJumping = False

    def update(self):
        if self.isJumping:
            self.movement[1] = self.movement[1] + gravity

        if self.isJumping:
            self.index = 0
        elif self.isBlinking:
            if self.index == 0:
                if self.counter % 400 == 399:
                    self.index = (self.index + 1)%2
            else:
                if self.counter % 20 == 19:
                    self.index = (self.index + 1)%2

        elif self.isDucking:
            if self.counter % 5 == 0:
                self.index = (self.index + 1)%2
        else:
            if self.counter % 5 == 0:
                self.index = (self.index + 1)%2 + 2

        if self.isDead:
           self.index = 4

        if not self.isDucking:
            self.image = self.images[self.index]
            self.rect.width = self.stand_pos_width
        else:
            self.image = self.images1[(self.index)%2]
            self.rect.width = self.duck_pos_width

        self.rect = self.rect.move(self.movement)
        self.checkbounds()

        if not self.isDead and self.counter % 7 == 6 and self.isBlinking == False:
            self.score += 1
            if self.score % 100 == 0 and self.score != 0:
                if pygame.mixer.get_init() != None:
                    checkPoint_sound.play()

        self.counter = (self.counter + 1)

class Cactus(pygame.sprite.Sprite):
    def __init__(self,speed=5,sizex=-1,sizey=-1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.images,self.rect = load_sprite_sheet('cacti-small.png',3,1,sizex,sizey,-1)
        self.rect.bottom = int(0.98*height)
        self.rect.left = width + self.rect.width
        self.image = self.images[random.randrange(0,3)]
        self.movement = [-1*speed,0]

    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()

class Ptera(pygame.sprite.Sprite):
    def __init__(self,speed=5,sizex=-1,sizey=-1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.images,self.rect = load_sprite_sheet('ptera.png',2,1,sizex,sizey,-1)
        self.ptera_height = [height*0.82,height*0.75,height*0.60]
        self.rect.centery = self.ptera_height[random.randrange(0,3)]
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1*speed,0]
        self.index = 0
        self.counter = 0

    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index+1)%2
        self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)
        self.counter = (self.counter + 1)
        if self.rect.right < 0:
            self.kill()

class Ground():
    def __init__(self,speed=-5):
        self.image,self.rect = load_image('ground.png',-1,-1,-1)
        self.image1,self.rect1 = load_image('ground.png',-1,-1,-1)
        self.rect.bottom = height
        self.rect1.bottom = height
        self.rect1.left = self.rect.right
        self.speed = speed

    def draw(self):
        screen.blit(self.image,self.rect)
        screen.blit(self.image1,self.rect1)

    def update(self):
        self.rect.left += self.speed
        self.rect1.left += self.speed

        if self.rect.right < 0:
            self.rect.left = self.rect1.right

        if self.rect1.right < 0:
            self.rect1.left = self.rect.right

class Cloud(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image,self.rect = load_image('cloud.png',int(90*30/42),30,-1)
        self.speed = 1
        self.rect.left = x
        self.rect.top = y
        self.movement = [-1*self.speed,0]

    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()

class Scoreboard():
    def __init__(self,x=-1,y=-1):
        self.score = 0
        self.tempimages,self.temprect = load_sprite_sheet('numbers.png',12,1,11,int(11*6/5),-1)
        self.image = pygame.Surface((55,int(11*6/5)))
        self.rect = self.image.get_rect()
        if x == -1:
            self.rect.left = width*0.89
        else:
            self.rect.left = x
        if y == -1:
            self.rect.top = height*0.1
        else:
            self.rect.top = y

    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self,score):
        score_digits = extractDigits(score)
        self.image.fill(background_col)
        for s in score_digits:
            self.image.blit(self.tempimages[s],self.temprect)
            self.temprect.left += self.temprect.width
        self.temprect.left = 0

class App(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        #pygame.display.iconify()
        self.act=''
        super(self.__class__,self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.frameThread = FrameThread(0,self.label_7,self.label_5)

        self.pushButton_4.clicked.connect(self.on_click)
        self.pushButton_3.clicked.connect(self.start_game)
        self.pushButton_5.clicked.connect(self.stop_cv)
        self.pushButton_5.setEnabled(False)
        
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()
        
        self.label_2.setPixmap(QtGui.QPixmap("sprites/logo.png"))
        
    def on_click(self):
        self.resize(905,317)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(True)
        self.frameThread.start()
        isGameQuit = self.introscreen(self.label_2)
        if not isGameQuit:
            self.gameplay(self.label_2,self.label_6,self.label_10)
            pygame.display.flip()
    
    def stop_cv(self):
        self.resize(637,317)
        self.frameThread.destoryed()
        self.label_5.setText('')
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(False)

    def start_game(self):
        self.resize(637,317)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        isGameQuit = self.introscreen(self.label_2)
        if not isGameQuit:
            self.gameplay(self.label_2,self.label_6,self.label_10)
            pygame.display.flip()
    
    def keyPressEvent(self,event):
        key=event.key()
        if key==QtCore.Qt.Key_Up or (event.type()==QtCore.QEvent.KeyPress and key==QtCore.Qt.Key_Space):
            self.act='space'
        if key==QtCore.Qt.Key_Down:
            self.act='down'      

    def displayTime(self):
        self.label_9.setText(QtCore.QDateTime.currentDateTime().toString())
    
    def introscreen(self,win):
        temp_dino = Dino(44,47)
        temp_dino.isBlinking = True
        gameStart = False

        temp_ground,temp_ground_rect = load_sprite_sheet('ground.png',15,1,-1,-1,-1)
        temp_ground_rect.left = width/20
        temp_ground_rect.bottom = height

        logo,logo_rect = load_image('logoa.png',300,140,-1)
        logo_rect.centerx = width*0.6
        logo_rect.centery = height*0.6
        while not gameStart:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                return True
            else:
                if self.act=='space':
                    temp_dino.isJumping=True
                    temp_dino.isBlinking=False
                    temp_dino.movement[1]=-1*temp_dino.jumpSpeed
                    self.act=''
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                            temp_dino.isJumping = True
                            temp_dino.isBlinking = False
                            temp_dino.movement[1] = -1*temp_dino.jumpSpeed

            temp_dino.update()

            if pygame.display.get_surface() != None:
                screen.fill(background_col)
                screen.blit(temp_ground[0],temp_ground_rect)
                if temp_dino.isBlinking:
                    screen.blit(logo,logo_rect)
                temp_dino.draw()

                pygame.display.update()

                data=screen.get_buffer().raw
                image=QtGui.QImage(data,width,height,QtGui.QImage.Format_RGB32)
                pixmap = QPixmap.fromImage(image)
                win.setPixmap(pixmap)

            clock.tick(FPS)
            if temp_dino.isJumping == False and temp_dino.isBlinking == False:
                gameStart = True
    
    def gameplay(self,win,score,hscore):
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        global high_score
        lastduck=0
        currentscr=0
        gamespeed = 4
        startMenu = False
        gameOver = False
        gameQuit = False
        playerDino = Dino(44,47)
        new_ground = Ground(-1*gamespeed)
        scb = Scoreboard()
        highsc = Scoreboard(width*0.78)
        counter = 0

        cacti = pygame.sprite.Group()
        pteras = pygame.sprite.Group()
        clouds = pygame.sprite.Group()
        last_obstacle = pygame.sprite.Group()

        Cactus.containers = cacti
        Ptera.containers = pteras
        Cloud.containers = clouds

        retbutton_image,retbutton_rect = load_image('replay_button.png',35,31,-1)
        gameover_image,gameover_rect = load_image('game_over.png',190,11,-1)

        temp_images,temp_rect = load_sprite_sheet('numbers.png',12,1,11,int(11*6/5),-1)
        HI_image = pygame.Surface((22,int(11*6/5)))
        HI_rect = HI_image.get_rect()
        HI_image.fill(background_col)
        HI_image.blit(temp_images[10],temp_rect)
        temp_rect.left += temp_rect.width
        HI_image.blit(temp_images[11],temp_rect)
        HI_rect.top = height*0.1
        HI_rect.left = width*0.73

        while not gameQuit:
            while startMenu:
                pass
            while not gameOver:
                if pygame.display.get_surface() == None:
                    print("Couldn't load display surface")
                    gameQuit = True
                    gameOver = True
                else:
                    if(self.label_5.text()!=''):
                        if(self.label_5.text()=='Up'):
                            self.act='space'
                        if(self.label_5.text()=='Down'):
                            self.act='down'
                    #KEYBOARD COMMAND FROM PYQT
                    currentscr=playerDino.score
                    if self.act=='space':
                        if playerDino.rect.bottom==int(0.98*height):
                            playerDino.isJumping=True
                            if pygame.mixer.get_init()!=None:
                                jump_sound.play()
                            playerDino.movement[1]=-1*playerDino.jumpSpeed
                            self.act=''
                    if self.act=='down':
                        if not (playerDino.isJumping and playerDino.isDead):
                            playerDino.isDucking=True
                            self.act=''
                            lastduck=playerDino.score
                    if not currentscr==0 and not lastduck ==0 and currentscr-lastduck>=0 and currentscr-lastduck<=1:
                        playerDino.isDucking=True
                    else:
                        playerDino.isDucking=False

                    #KEYBOARD COMMAND FROM PYGAME
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameQuit = True
                            gameOver = True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                if playerDino.rect.bottom == int(0.98*height):
                                    playerDino.isJumping = True
                                    if pygame.mixer.get_init() != None:
                                        jump_sound.play()
                                    playerDino.movement[1] = -1*playerDino.jumpSpeed

                            if event.key == pygame.K_DOWN:
                                if not (playerDino.isJumping and playerDino.isDead):
                                    playerDino.isDucking = True

                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_DOWN:
                                playerDino.isDucking = False
                for c in cacti:
                    c.movement[0] = -1*gamespeed
                    if pygame.sprite.collide_mask(playerDino,c):
                        playerDino.isDead = True
                        if pygame.mixer.get_init() != None:
                            die_sound.play()

                for p in pteras:
                    p.movement[0] = -1*gamespeed
                    if pygame.sprite.collide_mask(playerDino,p):
                        playerDino.isDead = True
                        if pygame.mixer.get_init() != None:
                            die_sound.play()

                if len(cacti) < 2:
                    if len(cacti) == 0:
                        last_obstacle.empty()
                        last_obstacle.add(Cactus(gamespeed,40,40))
                    else:
                        for l in last_obstacle:
                            if l.rect.right < width*0.7 and random.randrange(0,50) == 10:
                                last_obstacle.empty()
                                last_obstacle.add(Cactus(gamespeed, 40, 40))

                if len(pteras) == 0 and random.randrange(0,200) == 10 and counter > 500:
                    for l in last_obstacle:
                        if l.rect.right < width*0.8:
                            last_obstacle.empty()
                            last_obstacle.add(Ptera(gamespeed, 46, 40))

                if len(clouds) < 5 and random.randrange(0,300) == 10:
                    Cloud(width,random.randrange(height/5,height/2))

                playerDino.update()
                cacti.update()
                pteras.update()
                clouds.update()
                new_ground.update()
                scb.update(playerDino.score)
                score.setText(str(playerDino.score))
                highsc.update(high_score)

                if pygame.display.get_surface() != None:
                    screen.fill(background_col)
                    new_ground.draw()
                    clouds.draw(screen)
                    scb.draw()
                    if high_score != 0:
                        highsc.draw()
                        screen.blit(HI_image,HI_rect)
                    cacti.draw(screen)
                    pteras.draw(screen)
                    playerDino.draw()

                    pygame.display.update()

                    #Add to the Qt
                    data=screen.get_buffer().raw
                    image=QtGui.QImage(data,width,height,QtGui.QImage.Format_RGB32)
                    pixmap = QPixmap.fromImage(image)
                    win.setPixmap(pixmap)

                clock.tick(FPS)

                if playerDino.isDead:
                    gameOver = True
                    if playerDino.score > high_score:
                        high_score = playerDino.score
                        hscore.setText(str(high_score))

                if counter%700 == 699:
                    new_ground.speed -= 1
                    gamespeed += 1

                counter = (counter + 1)

            if gameQuit:
                break

            while gameOver:
                if pygame.display.get_surface() == None:
                    print("Couldn't load display surface")
                    gameQuit = True
                    gameOver = False
                else:
                    self.pushButton_3.setEnabled(True)
                    self.pushButton_4.setEnabled(True)
                    if self.act=='space':
                        gameOver=False
                        self.gameplay(win,score,hscore)
                        act=''

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameQuit = True
                            gameOver = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                gameQuit = True
                                gameOver = False

                            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                                gameOver = False
                                self.gameplay(win,score,hscore) 
                highsc.update(high_score)
                if pygame.display.get_surface() != None:
                    disp_gameOver_msg(retbutton_image,gameover_image)
                    if high_score != 0:
                        highsc.draw()
                        screen.blit(HI_image,HI_rect)
                    pygame.display.update()
                    data=screen.get_buffer().raw
                    image=QtGui.QImage(data,width,height,QtGui.QImage.Format_RGB32)
                    pixmap = QPixmap.fromImage(image)
                    win.setPixmap(pixmap)
                clock.tick(FPS)


def main():  
    app=QtWidgets.QApplication(sys.argv)
    form=App()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

"""GAME REFERENCE by Rohit Rane"""