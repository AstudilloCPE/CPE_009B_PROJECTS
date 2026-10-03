import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

# Create a class that displays the Window
class Fullname_Display(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    #Set the Window title and Size
    def initUI(self):
        self.setWindowTitle("Midterm in OOP")
        self.resize(500, 300)
        # Since we require two fields for the program, we use QGridLayout to Create a grid layout
        grid = QGridLayout()
        # Color the text in red
        color = "color: red;"
        # Asks the user to enter their full name 
        self.label1 = QLabel("Enter your fullname:")
        self.label1.setStyleSheet(color)
        # An Empty field
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your full name here...")

        self.btn = QPushButton("Click to display your Fullname")
        self.btn.setStyleSheet(color)
        self.btn.clicked.connect(self.display_name)

        self.output_field = QLineEdit()
        self.output_field.setReadOnly(True)

        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.input_field, 0, 1)
        grid.addWidget(self.btn, 1, 0)
        grid.addWidget(self.output_field, 1, 1)

        self.setLayout(grid)

    def display_name(self):
        name = self.input_field.text()
        self.output_field.setText(name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Fullname_Display()
    window.show()
    sys.exit(app.exec())