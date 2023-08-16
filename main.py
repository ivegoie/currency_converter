import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

app = QApplication(sys.argv)

widget = MainWindow()
widget.show()

app.exec()

