import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from TraditionalImageConverter import TraditionalImageConverter


class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome Screen")

        button_width = self.width() // 3
        button_height = self.height() // 2

        button_x_offset = (self.width() - button_width * 3) // 4
        button_y_offset = (self.height() - button_height) // 2

        button1 = QPushButton("Image Converter", self)
        button2 = QPushButton("HEIC Converter", self)
        button3 = QPushButton("Undefined", self)

        button1.setGeometry(button_x_offset, button_y_offset, button_width, button_height)
        button2.setGeometry(button_x_offset * 2 + button_width, button_y_offset, button_width, button_height)
        button3.setGeometry(button_x_offset * 3 + button_width * 2, button_y_offset, button_width, button_height)


        button1.clicked.connect(self.show_transitional_converter)

    def show_transitional_converter(self):
        self.traditional_converter = TraditionalImageConverter()
        self.traditional_converter.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WelcomeScreen()
    window.show()
    sys.exit(app.exec_())
