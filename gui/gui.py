import sys
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
 
 
# Define the welcome page.
class welcome(QWidget):

   def __init__(self, parent=None):
      super(welcome, self).__init__(parent)

      # create the widgets.
      # the title of the window.
      self.title = QLabel("Aggie Pass")
      # the second line of title
      self.title2 = QLabel("Please Scan Your RFID")
      # the third line of title
      self.title3 = QLabel("Please Enter Your PIN")
      # add the text edit bar, this will serve as the input box of PIN.
      self.edit = QLineEdit("Enter PIN")
      self.button_submit = QPushButton("SUBMIT")      # add the submit button
      self.button_register = QPushButton("REGISTER")  # add the submit button

      # modify the stylesheets of the titles.
      self.title.setStyleSheet("color: white; font: bold 25px")
      self.title2.setStyleSheet("color: white; font: bold 15px")
      self.title3.setStyleSheet("color: white; font: bold 15px")

      # modify the stylesheet of the edit bar.
      self.edit.setFixedWidth(400)
      self.edit.setFixedHeight(40)
      self.edit.setStyleSheet(
         "background-color: white; color: #800000; font: 14px; border-color: white")
      self.edit.setAlignment(Qt.AlignCenter)
      # Selects all the texts currently in the text box, so the new values will immediately replace the default.
      self.edit.selectAll()

      # modify the stylesheet of submission button.
      self.button_submit.clicked.connect(self.submission)
      self.button_submit.setStyleSheet(
         "background-color: white; color: #800000; font: bold 14px")
      self.button_submit.setFixedWidth(170)
      self.button_submit.setFixedHeight(60)

      # modify the stylesheet of registration button.
      self.button_register.clicked.connect(self.registration)
      self.button_register.setStyleSheet(
         "background-color: white; color: #800000; font: bold 12px")
      self.button_register.setFixedWidth(80)
      self.button_register.setFixedHeight(30)

      # create a layout fot he window, and then add the widgets to the layout.
      layout = QVBoxLayout(self)
      layout.addWidget(self.button_register, alignment=Qt.AlignRight)
      layout.addWidget(self.title, alignment=Qt.AlignCenter)
      layout.addWidget(self.title2, alignment=Qt.AlignCenter)
      layout.addWidget(self.title3, alignment=Qt.AlignCenter)
      layout.addWidget(self.edit, alignment=Qt.AlignCenter)
      layout.addWidget(self.button_submit, alignment=Qt.AlignCenter)

      # set the layout for the window
      self.setLayout(layout)

      # modify the stylesheet of the window
      self.showMaximized()
      self.setStyleSheet("background-color: #800000")
      self.setWindowFlag(Qt.FramelessWindowHint)

      # no registration window yet.
      self.reg = None

      # no management window yet.
      self.manage = None

   # This method is invoked by button click, it will be changed in the future.
   def submission(self):
      print(f"Hello, {self.edit.text()}")
      if self.manage == None:
         self.manage = manager()
         self.manage.show()
         self.close()
         self = None
      else:
         self.manage.close()
         self.manage = None

   # This method is invoked by button click, it will be changed in the future.
   def registration(self):
      if self.reg == None:
         self.reg = registration()
         self.reg.show()
         self.close()
         self = None
      else:
         self.reg.close()
         self.reg = None


# Define the registration page.
class registration(QWidget):
   def __init__(self, parent=None):
      super(registration, self).__init__(parent)

      # create the widgets.
      # the title of the window.
      self.title = QLabel("Registration")
      # the second line of title
      self.title2 = QLabel("Please Scan Your RFID")
      # the third line of title
      self.title3 = QLabel("Please Enter Your PIN")
      # add the text edit bar, this will serve as the input box of PIN.
      self.edit = QLineEdit("Enter PIN")
      self.button_submit = QPushButton("SUBMIT")      # add the submit button
      self.button_home = QPushButton("HOME")  # add the submit button

      # modify the stylesheets of the titles.
      self.title.setStyleSheet("color: white; font: bold 25px")
      self.title2.setStyleSheet("color: white; font: bold 15px")
      self.title3.setStyleSheet("color: white; font: bold 15px")

      # modify the stylesheet of the edit bar.
      self.edit.setFixedWidth(400)
      self.edit.setFixedHeight(40)
      self.edit.setStyleSheet(
         "background-color: white; color: #800000; font: 14px; border-color: white")
      self.edit.setAlignment(Qt.AlignCenter)
      # Selects all the texts currently in the text box, so the new values will immediately replace the default.
      self.edit.selectAll()

      # modify the stylesheet of submission button.
      self.button_submit.clicked.connect(self.submission)
      self.button_submit.setStyleSheet(
         "background-color: white; color: #800000; font: bold 14px")
      self.button_submit.setFixedWidth(170)
      self.button_submit.setFixedHeight(60)

      # modify the stylesheet of registration button.
      self.button_home.clicked.connect(self.home)
      self.button_home.setStyleSheet(
         "background-color: white; color: #800000; font: bold 12px")
      self.button_home.setFixedWidth(80)
      self.button_home.setFixedHeight(30)

      # create a layout fot he window, and then add the widgets to the layout.
      layout = QVBoxLayout(self)
      layout.addWidget(self.button_home, alignment=Qt.AlignRight)
      layout.addWidget(self.title, alignment=Qt.AlignCenter)
      layout.addWidget(self.title2, alignment=Qt.AlignCenter)
      layout.addWidget(self.title3, alignment=Qt.AlignCenter)
      layout.addWidget(self.edit, alignment=Qt.AlignCenter)
      layout.addWidget(self.button_submit, alignment=Qt.AlignCenter)

      # set the layout for the window
      self.setLayout(layout)

      # modify the stylesheet of the window
      self.showMaximized()
      self.setStyleSheet("background-color: #800000")
      self.setWindowFlag(Qt.FramelessWindowHint)

      # no home window yet.
      self.hm = None

   # This method is invoked by button click, it will be changed in the future.
   def submission(self):
      print(f"Hello, {self.edit.text()}")
      self.home()

   # This method is invoked by button click, it will be changed in the future.
   def home(self):
      if self.hm == None:
         self.hm = welcome()
         self.hm.show()
         self.close
         self = None
      else:
         self.hm.close()
         self.hm = None


data = {
        'acc_description':['dafergdsgagdadsa1234', 'dsa4dsa32dgsat4', '2fdsat4eadfa454', '2efdsa4ty5yhts', 'dsa234gdfsa4ytqa'],
        'acc_username':['sa2rfdsa32gsa', 'a32t2dsa4tf', '2rgdfsaaw34gra', 'as32fdsa4ygfdsa', 'q2fdsa32ytgfdas'],
        'acc_password':['2esda32tdsa3tgrsae312sa3', 'as4esagesa32afdsafdsa', '1ea43wadasf43ag4a4', '2gsa33at4afdsa', '23ta4a4ygs4ay4afds'] 
        }
df = pd.DataFrame(data)
pass_data = df.to_numpy()
print(pass_data)

# Define the manager page.
class manager(QWidget):
   def __init__(self, parent=None):
      super(manager, self).__init__(parent)

      self.button_home = QPushButton("HOME")      # add the home button

      # modify the stylesheet of homebutton.
      self.button_home.clicked.connect(self.home)
      self.button_home.setStyleSheet("background-color: white; color: #800000; font: bold 12px")
      self.button_home.setFixedWidth(80)
      self.button_home.setFixedHeight(30)

      # create a layout fot he window, and then add the widgets to the layout.
      layout = QVBoxLayout(self)
      layout.addWidget(self.button_home, alignment=Qt.AlignRight)

      layout_h = QHBoxLayout()
      layout_h.addWidget(self.createTable(), stretch = 1, alignment=Qt.AlignCenter)

      layout.addLayout(layout_h)

      # set the layout for the window
      self.setLayout(layout)

      # modify the stylesheet of the window
      self.showMaximized()
      self.setStyleSheet("background-color: #800000")
      self.setWindowFlag(Qt.FramelessWindowHint)

      # no home window yet.
      self.hm = None

   # This method is invoked by button click, it will be changed in the future.
   def home(self):
      if self.hm == None:
         self.hm = welcome()
         self.hm.show()
         self.close
         self = None
      else:
         self.hm.close()
         self.hm = None
   
   # This method is to create a table for passwords, and user names, etc.
   def createTable(self):
      # initailize a table object.
      self.tableWidget = QTableWidget()
      
      # this line prevents triggering edit once clicked on the cell.
      self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

      # controls the scollbars.
      # self.tableWidget.verticalHeader().setVisible(False)
      # self.tableWidget.horizontalScrollBar().setDisabled(True)
      # self.tableWidget.horizontalScrollBar().setVisible(False)

      # sets the size of the table, we need to manually change the width and height to make it fill the window.
      self.tableWidget.setFixedWidth(460)
      self.tableWidget.setFixedHeight(150)

      # row and column count.
      self.tableWidget.setRowCount(len(df.acc_username))
      self.tableWidget.setColumnCount(3)

      # set the column headers.
      idx = 0
      for i in df.columns.values:
         self.tableWidget.setHorizontalHeaderItem(idx, QTableWidgetItem(i))
         idx += 1

      # set the cell values.
      for i in range(self.tableWidget.rowCount()):
         for j in range(self.tableWidget.columnCount()):
            self.tableWidget.setItem(i,j, QTableWidgetItem(pass_data[i][j]))
      
      # stretch the header view to fill the window. 
      # still need to set the size of table, this line only makes the table fill the rectangle with fixed size.
      self.tableWidget.horizontalHeader().setStretchLastSection(True)
      self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
      self.tableWidget.setSelectionBehavior(QTableView.SelectRows)
      return self.tableWidget

def main():
   app = QApplication(sys.argv)
   screen = app.primaryScreen()
   print('Screen: %s' % screen.name())
   rect = screen.availableGeometry()
   print('Available: %d x %d' % (rect.width(), rect.height()))
   ex = welcome()
   ex.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   main()
