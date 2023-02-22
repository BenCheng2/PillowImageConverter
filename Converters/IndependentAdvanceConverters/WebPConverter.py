import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QApplication
from PyQt5.QtGui import QPixmap
from PIL import Image

class WebPConverter(QWidget):
    file_label: QLabel
    file_load_button: QPushButton
    image_label: QLabel
    convert_button_group: QHBoxLayout

    found_image: str

    jpg_button: QPushButton
    jpeg_button: QPushButton
    jpe_button: QPushButton
    jxr_button: QPushButton
    png_button: QPushButton
    tif_button: QPushButton
    tiff_button: QPushButton
    bmp_button: QPushButton

    def __init__(self):
        super().__init__()

        self.setWindowTitle("WebP Converter")

        self.file_label = QLabel("Select a file to convert:")

        self.file_load_button = QPushButton("Open file")

        self.image_label = QLabel()
        self.setGeometry(100, 100, 1000, 1000)
        self.image_label.setMinimumSize(800, 800)

        self.convert_button_group = QHBoxLayout()
        self.jpg_button = QPushButton("Convert to JPG")
        self.jpeg_button = QPushButton("Convert to JPEG")
        self.jpe_button = QPushButton("Convert to JPE")
        self.jxr_button = QPushButton("Convert to JXR")
        self.png_button = QPushButton("Convert to PNG")
        self.tif_button = QPushButton("Convert to TIF")
        self.tiff_button = QPushButton("Convert to TIFF")
        self.bmp_button = QPushButton("Convert to BMP")

        self.convert_button_group.addWidget(self.jpg_button)
        self.convert_button_group.addWidget(self.jpeg_button)
        self.convert_button_group.addWidget(self.jpe_button)
        self.convert_button_group.addWidget(self.jxr_button)
        self.convert_button_group.addWidget(self.png_button)
        self.convert_button_group.addWidget(self.tif_button)
        self.convert_button_group.addWidget(self.tiff_button)
        self.convert_button_group.addWidget(self.bmp_button)


        # Add the element to the widget
        layout = QVBoxLayout()
        layout.addWidget(self.file_label, 1)
        layout.addWidget(self.file_load_button, 1)
        layout.addWidget(self.image_label, 6)
        layout.addLayout(self.convert_button_group, 2)
        self.setLayout(layout)

        self.file_load_button.clicked.connect(self.open_file)

        self.jpg_button.clicked.connect(self.convert_to_jpg)
        self.jpeg_button.clicked.connect(self.convert_to_jpeg)
        self.jpe_button.clicked.connect(self.convert_to_jpe)
        self.jxr_button.clicked.connect(self.convert_to_jxr)
        self.png_button.clicked.connect(self.convert_to_png)
        self.tif_button.clicked.connect(self.convert_to_tif)
        self.tiff_button.clicked.connect(self.convert_to_tiff)
        self.bmp_button.clicked.connect(self.convert_to_bmp)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open WebP Image", "", "WebP Image (*.webp)")
        if file_path:
            self.load_image(file_path)
            self.found_image = file_path

    def load_image(self, file_path):
        pixmap = QPixmap(file_path)
        scaled_image = pixmap.scaled(self.image_label.size(), aspectRatioMode=Qt.KeepAspectRatio)
        self.image_label.setPixmap(scaled_image)
        self.image_label.setAlignment(Qt.AlignCenter)

    def convert_to_jpg(self):
        self._convert_format_helper("Convert to JPG", "JPG Image (*.jpg)", "JPG")

    def convert_to_jpeg(self):
        self._convert_format_helper("Convert to JPEG", "JPEG Image (*.jpeg)", "JPEG")

    def convert_to_jpe(self):
        self._convert_format_helper("Convert to JPE", "JPE Image (*.jpe)", "JPE")

    def convert_to_jxr(self):
        self._convert_format_helper("Convert to JXR", "JXR Image (*.jxr)", "JXR")

    def convert_to_png(self):
        self._convert_format_helper("Convert to PNG", "PNG Image (*.png)", "PNG")

    def convert_to_tif(self):
        self._convert_format_helper("Convert to TIF", "TIF Image (*.tif)", "tif")

    def convert_to_tiff(self):
        self._convert_format_helper("Convert to TIFF", "TIFF Image (*.tiff)", "tiff")

    def convert_to_bmp(self):
        self._convert_format_helper("Convert to BMP", "BMP Image (*.bmp)", "bmp")


    def _convert_format_helper(self, message, file_type, file_extension):
        file_path, _ = QFileDialog.getSaveFileName(self, message, "", file_type)
        if file_path:
            image = Image.open(self.found_image)
            image.save(file_path, file_extension)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = WebPConverter()
    main_window.show()
    sys.exit(app.exec_())