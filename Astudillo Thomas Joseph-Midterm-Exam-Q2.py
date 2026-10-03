import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

# Class for the Window
class ChangeColor_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the Window Title and Size
        self.setWindowTitle("Special Midterm Exam in OOP")
        self.resize(450, 350)
        # Create the push button to change the color
        self.btn = QPushButton("Click to Change Color", self)
        self.btn.setFixedSize(160, 35)
        # Move button to the middle of the window
        self.btn.move(145, 155)
        # Connect the change_color function to the QPushButton
        # On click, the button should be recolored
        self.btn.clicked.connect(self.change_color)

    # Change color function
    # setStyleSheet allows the background color to be set to any valid color name
    # In this case we use the color yellow to change the buttons background to yellow on click
    def change_color(self):
        self.btn.setStyleSheet("background-color: yellow;")

# Code to run the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChangeColor_Window()
    window.show()
    sys.exit(app.exec())