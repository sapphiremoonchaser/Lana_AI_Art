# Imports
import sys
from locale import windows_locale
from wsgiref.util import application_uri

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout, QBoxLayout, QLineEdit,
)

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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())