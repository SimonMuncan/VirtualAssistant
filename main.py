from PyQt5.QtWidgets import QApplication
import sys
from assistantGUI import *

# Create an instance of QApplication to manage the GUI application
app = QApplication(sys.argv)
# Create an instance of the MainWindow class
window = MainWindow()
# Show the main window
window.show()

app.exec()