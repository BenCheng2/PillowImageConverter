from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PIL import Image

class TraditionalImageConverter(QWidget):
    file_label: QLabel
    file_load_button: QPushButton
    image_label: QLabel
    convert_button_group: QHBoxLayout
    found_image: str
    traditional_converter: QWidget

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
        print(1)
        self.setWindowTitle("Image Converter")
        self.setGeometry(100, 100, 1000, 1000)

        self.file_label = QLabel("Select a file to convert:")
        self.file_load_button = QPushButton("Open file")
        self.image_label = QLabel()
        self.image_label.setMinimumSize(800, 800)
        self.convert_button_group = QHBoxLayout()
        print(2)
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
        print(3)
        layout = QVBoxLayout()
        layout.addWidget(self.file_label, 1)
        layout.addWidget(self.file_load_button, 1)
        layout.addWidget(self.image_label, 6)
        layout.addLayout(self.convert_button_group, 2)
        print(4)
        self.setLayout(layout)

        self.file_load_button.clicked.connect(self.open_file)
        print(5)
        self.jpg_button.clicked.connect(self.convert_to_jpg)
        self.jpeg_button.clicked.connect(self.convert_to_jpeg)
        self.jpe_button.clicked.connect(self.convert_to_jpe)
        self.jxr_button.clicked.connect(self.convert_to_jxr)
        self.png_button.clicked.connect(self.convert_to_png)
        self.tif_button.clicked.connect(self.convert_to_tif)
        self.tiff_button.clicked.connect(self.convert_to_tiff)
        self.bmp_button.clicked.connect(self.convert_to_bmp)
        print(6)

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

            self.show_image(file_path)

    def show_image(self, path):
        pixmap = QPixmap(path)

        scaled_image = pixmap.scaled(self.image_label.size(), aspectRatioMode=Qt.KeepAspectRatio)

        self.image_label.setPixmap(scaled_image)

    def convert_to_jpg(self):
        # By the way, the jpeg works the same way
        self._convert_format_helper("JPG files (*.jpg)", "jpg")

    def convert_to_jpeg(self):
        self._convert_format_helper("JPEG files (*.jpeg)", "jpeg")

    def convert_to_jpe(self):
        self._convert_format_helper("JPE files (*.jpe)", "jpe")

    def convert_to_jxr(self):
        self._convert_format_helper("JXR files (*.jxr)", "jxr")

    def convert_to_png(self):
        self._convert_format_helper("PNG files (*.png)", "png")

    def convert_to_tif(self):
        self._convert_format_helper("TIF files (*.tif)", "tif")

    def convert_to_tiff(self):
        self._convert_format_helper("TIFF files (*.tiff)", "tiff")

    def convert_to_bmp(self):
        self._convert_format_helper("BMP files (*.bmp)", "bmp")

    def _convert_format_helper(self, name_format, suffix):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter(name_format)
        file_dialog.selectNameFilter(name_format)
        file_dialog.setDefaultSuffix(suffix)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setViewMode(QFileDialog.Detail)

        # If user picked a position to save the image
        if file_dialog.exec_():
            # Extract the file path
            file_path = file_dialog.selectedFiles()[0]

            # Open the image
            image = Image.open(self.found_image)

            # Save the file
            image.save(file_path)
