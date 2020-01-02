# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 20:48:15 2019

@author: Dean
"""

import time
import RPi.GPIO as GPIO #基本的GPIO控制功能
import cv2
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime

def mail():
    to = '＊＊＊＊＊@gmail.com'
    gmail_user = '＊＊＊＊＊＊@gmail.com'
    gmail_password = '＊＊＊＊'
    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_password)
    today = datetime.date.today()
    # Very Linux Specific
    arg='someone'
    my_msg = 'Someone come on'
    msg = MIMEText(my_msg)
    msg['Subject'] = 'warning'
    msg['From'] = gmail_user
    msg['To'] = to
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()
    
MONITOR_PIN = 18 #定義PIR輸出所連連接的腳位，BCM編號為18
 
GPIO.setmode(GPIO.BCM) #BCM編號方式
GPIO.setup(MONITOR_PIN, GPIO.IN) #將PIR輸出所使用的腳位設定為輸入模式
 
try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        if(GPIO.input(MONITOR_PIN) == 1): #當感測器偵測到物體，將會寄信到email並且開始錄影
            print("start")
            mail()
	    cap = cv2.VideoCapture(0)

	    # 設定擷取影像的尺寸大小
	    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
	    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

	    # 使用 XVID 編碼
	    fourcc = cv2.VideoWriter_fourcc(*'X264')

	    # 建立 VideoWriter 物件，輸出影片至 output.avi
	    # FPS 值為 20.0，解析度為 640x360
            dt = time.localtime()
            name = str(dt.tm_year) + '_' + str(dt.tm_mon) + '_' + str(dt.tm_mday) + '_' + str(dt.tm_hour) + str(dt.tm_min) + str(dt.tm_sec)
	    out = cv2.VideoWriter("/var/www/html/public/video/" + name +  '.mp4', fourcc, 20.0, (640, 360))
            now = time.time()
            future = now + 20  
	    while(cap.isOpened()):
		 ret, frame = cap.read()
		 if(ret == True):
	    	    # 寫入影格
		    out.write(frame)
                
		    if(time.time() > future):
		        break
		 else:
		    break

		    # 釋放所有資源
	    cap.release()
	    out.release()
	    cv2.destroyAllWindows()
        time.sleep(0.5)
except KeyboardInterrupt:
    print('關閉程式')
finally:
    GPIO.cleanup()
