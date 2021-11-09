import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window(QWidget):
      
   def __init__(self, parent = None):
      super(window, self).__init__(parent)

      # create the widgets.
      self.title = QLabel("Aggie Pass")               # the title of the window.
      self.title2 = QLabel("Please Scan Your RFID")   # the second line of title
      self.title3 = QLabel("Please Enter Your PIN")   # the third line of title
      self.edit = QLineEdit("Enter PIN")              # add the text edit bar, this will serve as the input box of PIN.
      self.button_submit = QPushButton("SUBMIT")      # add the submit button
      self.button_register = QPushButton("Register")  # add the submit button

      # modify the stylesheets of the titles.
      self.title.setStyleSheet("color: white; font: bold 50px")
      self.title2.setStyleSheet("color: white; font: bold 30px")
      self.title3.setStyleSheet("color: white; font: bold 30px")

      # modify the stylesheet of the edit bar.
      self.edit.setFixedWidth(400)
      self.edit.setFixedHeight(40)
      self.edit.setStyleSheet("background-color: white; color: #800000; font: 14px; border-color: white")
      self.edit.setAlignment(Qt.AlignCenter)

      # modify the stylesheet of submission button.
      self.button_submit.clicked.connect(self.submission)
      self.button_submit.setStyleSheet("background-color: white; color: #800000; font: bold 14px")
      self.button_submit.setFixedWidth(170)
      self.button_submit.setFixedHeight(60)
      
      # modify the stylesheet of registration button.
      self.button_register.clicked.connect(self.registration)
      self.button_register.setStyleSheet("background-color: white; color: #800000; font: bold 12px")
      self.button_register.setFixedWidth(80)
      self.button_register.setFixedHeight(30)

      # create a layout fot he window, and then add the widgets to the layout.
      layout = QVBoxLayout(self)
      layout.addWidget(self.button_register, alignment = Qt.AlignRight)
      layout.addWidget(self.title, alignment = Qt.AlignCenter)
      layout.addWidget(self.title2, alignment = Qt.AlignCenter)
      layout.addWidget(self.title3, alignment = Qt.AlignCenter)
      layout.addWidget(self.edit, alignment = Qt.AlignCenter)
      layout.addWidget(self.button_submit, alignment = Qt.AlignCenter)
      
      # set the layout for the window
      self.setLayout(layout)

      # modify the stylesheet of the window
      self.showMaximized()
      self.setStyleSheet("background-color: #800000")
      self.setWindowFlag(Qt.FramelessWindowHint)

   # This method is invoked by button click, it will be changed in the future.
   def submission(self):
      print(f"Hello, {self.edit.text()}")

   # This method is invoked by button click, it will be changed in the future.
   def registration(self):
      print(f"Registration Complete")

def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()