from PyQt5.QtWidgets import QApplication, QFileDialog
from PIL import Image

# Create a PyQt application
app = QApplication([])

# Get the input WebP file name using a file dialog box
webp_file, _ = QFileDialog.getOpenFileName(None, "Open WebP Image", "", "WebP Image (*.webp)")

# Get the output file name and location using a file dialog box
output_file, _ = QFileDialog.getSaveFileName(None, "Save Image As", "", "PNG Image (*.png)")

# If the user cancels the file dialog boxes, return
# if not webp_file or not output_file:

# Open the WebP image
webp_image = Image.open(webp_file)

# Save the image in a different format with the user-specified file name and location
webp_image.save(output_file, "png")

# Quit the PyQt application
app.quit()