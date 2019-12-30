# Get-Away-From-Me  

# 動機發想  
隨著台灣經濟的不斷發展與女權主義的抬頭，目前國內具有獨立經濟能力的女性已非少數，而為了賺錢謀生居住於異地他鄉亦是常態，然而獨居女性的安全不容忽視，故而設想開發一套簡易偵測系統，若有人經過房門前便錄影存證並發出提醒，藉以提升獨居女性的危機意識，縱有提況也能第一時間應對。
# 所需設備  
* Raspberry pi 3 （課程提供）   
* 紅外線感測器 （課程提供）  
* Logitch C270 HD WEBCAM （組員提供）

# 連接方式
![image](https://github.com/katherinegeorge/Get-Away-From-Me-/blob/master/%E6%88%AA%E5%9C%96%202019-12-30%20%E4%B8%8B%E5%8D%888.19.14.png)

# 系統架構
* Python3  
* Apache2 + PHP  

# 安裝套件
* time  
* RPi.GPIO   
* cv2  
* subprocess  
* smtplib  
* email.mine.text import MIMEText   
* datetime  

# 機身
![image](https://github.com/katherinegeorge/Get-Away-From-Me-/blob/master/189630.jpg)      
![image](https://github.com/katherinegeorge/Get-Away-From-Me-/blob/master/189632.jpg)    

# 網頁設計
![image](https://github.com/katherinegeorge/Get-Away-From-Me-/blob/master/1577711424204.jpg)  

# 工作分配表
* 朱家慶 - 題目發想、材料收集  
* 簡鈺紋 - 文件撰寫、題目發想  
* 黃名玄 - 程式開發

# 踩雷
！要注意套件中選擇相機的參數
# Reference
[Raspberry Pi 3 Model 紅外線偵測程式](https://blog.everlearn.tw/%E7%95%B6-python-%E9%81%87%E4%B8%8A-raspberry-pi/raspberry-pi-3-model-b-%E4%BD%BF%E7%94%A8-pir-%E7%9B%A3%E6%B8%AC%E7%A7%BB%E5%8B%95%E7%9A%84%E7%89%A9%E9%AB%94)  
