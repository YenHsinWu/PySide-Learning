import sys
from PySide6.QtWidgets import QApplication, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()

    app.exec()