import sys
import os

import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg


class ClickedLabel(qtw.QLabel):
    clicked = qtc.pyqtSignal(qtc.QEvent)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.clicked.emit(event)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MyTube')
        self.setGeometry(300, 300, 500, 300)
        self.__create_layouts()
        self.__create_widgets()
        self.show()
    
    def __create_layouts(self):
        self.main_layout = qtw.QHBoxLayout()
        
        self.toolbar_layout = qtw.QVBoxLayout()
        self.search_layout = qtw.QHBoxLayout()
        self.videos_layout = qtw.QGridLayout()

        self.search_and_videos_layout = qtw.QVBoxLayout()

        self.search_and_videos_layout.addLayout(self.search_layout)
        self.search_and_videos_layout.addLayout(self.videos_layout)
        self.main_layout.addLayout(self.search_and_videos_layout)
        self.main_layout.addLayout(self.toolbar_layout)

    def __create_widgets(self):
        self.main_widget = qtw.QWidget()
        self.main_widget.setStyleSheet("background-color: white;")
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        self.__create_search_widgets()
    
    def __create_search_widgets(self):
        self.mytube_label = ClickedLabel()
        self.mytube_label.setPixmap(qtg.QPixmap(os.path.join(os.path.dirname(__file__), 'Resources/mytube_icon.png')))
        self.search_layout.addWidget(self.mytube_label)



    

        
        
        
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
