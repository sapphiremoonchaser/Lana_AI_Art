# Imports
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel
)

from pipeline import initailize_pipeline

# Create a simple window with a title and a basic layout
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lana Del Rey Album Art Generator")
        self.setGeometry(100, 100, 800, 600)

        # Central Widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Add prompt input field
        self.prompt_input = QLineEdit()
        self.prompt_input.setPlaceholderText("Enter prompt (e.g., 'Lana Del Rey vintage aesthetic, dreamy beach')")
        self.layout.addWidget(self.prompt_input)

        # Add a button to trigger the art generation
        self.generate_btn = QPushButton("Generate Art")
        self.generate_btn.clicked.connect(self.generate_art)
        self.layout.addWidget(self.generate_btn)

        # Add area to show the generated image
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        # Initialize stable diffusion pipeline
        self.pipe = initailize_pipeline()
        if self.pipe is None:
            self.image_label.setText("Failed to load model. Check token and dependencies.")

    def generate_art(self):
        """Placeholder function for generating art."""
        prompt = self.prompt_input.text()
        if not prompt or not self.pipe:
            self.image_label.setText("Please enter a prompt and ensure model is loaded.")
            return

        try:
            print(f"Generating art with prompt: {prompt}")
            # Generate image with Stable Diffusion
            image = self.pipe(prompt, num_inference_steps=20).images[0]

            # Convert directly to QImage without temporary file
            data = image.convert("RGB").tobytes()
            qimage = QImage(data, image.width, image.height, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
            self.image_label.setPixmap(pixmap.scaled(512, 512, Qt.KeepAspectRatio))

        except Exception as e:
            self.image_label.setText(f"Error generating art: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
