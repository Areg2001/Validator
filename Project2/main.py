from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import main_window
import isvalid

class StartWindow(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.text = None
        self.check_type = None
        
        self.btn_check.clicked.connect(self.clickedd)

    def clickedd(self):
        self.text = self.line_edit.text()
        self.check_type = self.combo_box.currentText()
        if self.check_type == 'Email':
            valid = isvalid.isValidEmail(self.text)
        elif self.check_type == 'URL':
            valid = isvalid.isValidUrl(self.text)
        elif self.check_type == 'Date':
            valid = isvalid.isValidDate(self.text)
        elif self.check_type == 'Number':
            valid = isvalid.isValidNumber(self.text)
        elif self.check_type == 'Credit Card':
            valid = isvalid.isValidCreditCardNumber(self.text)
        elif self.check_type == 'Phone Number':
            valid = isvalid.isValidMobilePhoneNumber(self.text)

        if valid:
            message = f'Your {self.check_type} is valid'
        else:
            message = f'Your {self.check_type} is not valid'
        QMessageBox.about(self, "", message)
        
app = QApplication([])

widget = StartWindow()
widget.show()

app.exec()