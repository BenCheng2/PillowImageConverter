import sys

import PIL
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QApplication
from PyQt5.QtGui import QPixmap
from PIL import Image

class AdvancedImageConverter(QWidget):
    file_label: QLabel
    file_load_button: QPushButton
    image_label: QLabel
    convert_button_group: QHBoxLayout
    found_image: str


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Converter")
        self.setGeometry(100, 100, 1000, 1000)

        self.file_label = QLabel("Select a file to convert:")
        self.file_load_button = QPushButton("Open file")
        self.image_label = QLabel()
        self.image_label.setMinimumSize(800, 800)
        self.convert_button_group = QHBoxLayout()


        layout = QVBoxLayout()
        layout.addWidget(self.file_label, 1)
        layout.addWidget(self.file_load_button, 1)
        layout.addWidget(self.image_label, 6)
        layout.addLayout(self.convert_button_group, 2)
        self.setLayout(layout)

        self.file_load_button.clicked.connect(self.open_file)


        self.convert_button_group = QHBoxLayout()





    def open_file(self):
        file_dialog = QFileDialog(self)

        file_dialog.setNameFilter("Image files (*.jpg *.jpeg *.jpe *.jxr *.png *.tif *.tiff *.bmp *.heic)")
        file_dialog.selectNameFilter("Image files (*.jpg *.jpeg *.jpe *.jxr *.png *.tif *.tiff *.bmp)")
        file_dialog.setDefaultSuffix("jpg")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setViewMode(QFileDialog.Detail)

        # If user picked an image
        if file_dialog.exec_():
            # Extract the file path
            file_path = file_dialog.selectedFiles()[0]

            # Store the path to the found image
            self.found_image = file_path

    def show_image(self, path):
        image = Image.open(path)
        pixmap = QPixmap.fromImage(ImageQt(image))

        scaled_image = pixmap.scaled(self.image_label.size(), aspectRatioMode=Qt.KeepAspectRatio)

        self.image_label.setPixmap(scaled_image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedImageConverter()
    window.show()
    sys.exit(app.exec_())