import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow
from vi_calc import *

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calculadora()
        self.ui.setupUi(self)
        self.ui.button_0.clicked.connect(lambda: self.button_clicked("0"))
        self.ui.button_1.clicked.connect(lambda: self.button_clicked("1"))
        self.ui.button_2.clicked.connect(lambda: self.button_clicked("2"))
        self.ui.button_3.clicked.connect(lambda: self.button_clicked("3"))
        self.ui.button_4.clicked.connect(lambda: self.button_clicked("4"))
        self.ui.button_5.clicked.connect(lambda: self.button_clicked("5"))
        self.ui.button_6.clicked.connect(lambda: self.button_clicked("6"))
        self.ui.button_7.clicked.connect(lambda: self.button_clicked("7"))
        self.ui.button_8.clicked.connect(lambda: self.button_clicked("8"))
        self.ui.button_9.clicked.connect(lambda: self.button_clicked("9"))    
        self.ui.button_plus.clicked.connect(lambda: self.button_clicked("+"))
        self.ui.button_minus.clicked.connect(lambda: self.button_clicked("-"))
        self.ui.button_multiply.clicked.connect(lambda: self.button_clicked("*"))
        self.ui.button_divide.clicked.connect(lambda: self.button_clicked("/"))
        self.ui.button_comma.clicked.connect(lambda: self.button_clicked("."))
        self.ui.button_delete.clicked.connect(self.delete_last_character)
        self.ui.button_reset.clicked.connect(self.clear_display)
        self.ui.button_equal.clicked.connect(self.calculate_result)

    def button_clicked(self, button_value):
        current_text = self.ui.display.text()
        new_text = current_text + button_value
        self.ui.display.setText(new_text)

    def delete_last_character(self):
        current_text = self.ui.display.text()
        new_text = current_text[:-1]
        self.ui.display.setText(new_text)
    
    def clear_display(self):
        self.ui.display.setText("")
    
    def calculate_result(self):
        expression = self.ui.display.text()
        try:
            result = eval(expression)
            self.ui.display.setText(str(result))
        except Exception as e:
            self.ui.display.setText("Error")

if __name__ == "__main__":
    print("Arranco")
    app = QApplication(sys.argv)
    window = Calculadora()
    
    window.show()
    sys.exit(app.exec())
