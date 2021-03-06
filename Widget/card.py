from email import message
from fileinput import filename
from turtle import title
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem, QAbstractItemView, QMessageBox
from Widget.id import Ui_Idcard
import sqlite3
import smtplib
# import pyautogui
from email.mime.text import MIMEText
from PyQt5.QtGui import QPixmap

class AccountPage_ID(QMainWindow, Ui_Idcard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_photo_btn.clicked.connect(self.openfile)
        self.refresh_btn.clicked.connect(self.refreshitems)
        self.search_btn.clicked.connect(self.serachresults)
        self.register_btn.clicked.connect(self.tablereults)
        # self.capture.clicked.connect(self.myscreenshot)
        self.take_screen.clicked.connect(self.take_to_next)
        self.back_btn_2.clicked.connect(self.back2)
        self.save_page.clicked.connect(self.save)
        

    def openfile(self):
        global img
        fimg = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\jahei\\OneDrive\\Bureau\\ID\\Static', 'Image files (*.jpg *.png)')
        img = fimg[0]
        pixmap = QPixmap(img)
        self.add_photo.setPixmap(QPixmap(pixmap))
        self.add_photo.setScaledContents(True)
        return fimg[0]
      
        
    def tablereults(self):
        
        db = sqlite3.connect("userdata.db")
    
        dic = {
            "Prenom":self.prenom_line.text(),
            "Nom": self.nom_line.text(),
            "Sexe": self.comboBox.currentText(),
            "date":self.dateEdit_combo.text(),
            "img": img, 
            "email": self.email_line.text()
        }
        
        if self.prenom_line.text() == "" or self.nom_line.text() == "" or self.email_line.text() == "":
            QMessageBox.warning(self, "Error", "Veuillez saisir vos infomations")
        
        else:
            cur = db.cursor()
            cur.execute(""" CREATE TABLE IF NOT EXISTS User(
                        Prenom TEXT, 
                        Nom TEXT, 
                        Sexe TEXT, 
                        date TEXT,
                        email TEXT, 
                        img TEXT
                    )""")

        
            cur.execute("INSERT INTO User (Prenom, Nom, Sexe, date, email, img ) VALUES (?,?,?,?,?,?)", (dic["Prenom"],dic["Nom"],dic["Sexe"],dic["date"],dic["email"],dic["img"]))
            
            db.commit()
            db.close()
            
            title = "Carte D'identit??"
            msg_content = "<h2><font color = ""green"">Votre Carte D'identit?? a ??t?? valid??e avec succ??s pour plus d'informations appelez le +225 01 43 50 48 13 </font></h2>\n".format(title = title)
            message = MIMEText(msg_content, 'html')
            message['From'] = 'Jaheim Kouaho <jaheimkouaho@gmail.com>'
            message['Subject'] = "Carte D'identit??"
            msg_full = message.as_string()
            
            
            sever = smtplib.SMTP('smtp.gmail.com:587')
            sever.starttls()
            sever.login('jaheimkouaho@gmail.com', 'kwlwqgiycesfgukn')
            sever.sendmail('jaheimkouaho@gmail.com', [self.email_line.text()], msg_full,)
            sever.quit()
            
            self.prenom_line.clear()
            self.nom_line.clear()
            self.comboBox.clear()
            self.dateEdit_combo.clear()
            self.add_photo.clear()
            self.email_line.clear()
                        
            self.stackedWidget.setCurrentWidget(self.page)
            self.show()
        
                

    def back(self):
        
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.show()

    def save(self):
        
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.show()
    
    def refreshitems(self):
        
        dbs = sqlite3.connect("userdata.db")
        cut = dbs.cursor()
        command =''' SELECT * FROM User ''' 
        res = cut.execute(command)
        self.table.setRowCount(0)

        for row_number, row_data in enumerate(res):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    
    def serachresults(self):
        
        db = sqlite3.connect("userdata.db")
        cur = db.cursor()
        word = self.search_line.text()

        command = ''' SELECT * FROM User WHERE Prenom=? ''' 
        res = cur.execute(command,[word])
        self.table.setRowCount(0)

        for row_number, row_data in enumerate(res):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
    def take_to_next(self):    
        self.stackedWidget.setCurrentWidget(self.page_3)
        self.show()
        
    def back2(self): 
        self.stackedWidget.setCurrentWidget(self.page)
        self.show()   
        
    
        

    # def image(self):
        
    #     with mss.mss() as sct:
    #         # The screen part to capture
    #         monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
    #         output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    #         # Grab the data
    #         sct_img = sct.grab(monitor)

    #         # Save to the picture file
    #         mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    #         print(output)
    
    


        
        

    


    # def myscreenshot(self):
    #     myScreenshot = pyautogui.screenshot()
    #     myScreenshot.save(r'C:\Users\jahei\OneDrive\Bureau\ID\Static\screenshot.png')