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
        self.search_layout.addSpacing(10)

        self.mytube_label = ClickedLabel()
        self.mytube_label.setPixmap(qtg.QPixmap(os.path.join(os.path.dirname(__file__), 'Resources/mytube_icon.png')))
        self.mytube_label.setFixedSize(110, 65)
        self.mytube_label.setScaledContents(True)
        self.search_layout.addWidget(self.mytube_label)

        self.spacer_widget = qtw.QWidget()
        self.spacer_widget.setSizePolicy(qtw.QSizePolicy.Policy.Expanding, qtw.QSizePolicy.Policy.Preferred)
        self.spacer_widget.setMinimumWidth(50)
        self.spacer_widget.setMaximumWidth(400)
        self.search_layout.addWidget(self.spacer_widget)
        
        self.search_line = qtw.QLineEdit(self)
        self.search_line.setPlaceholderText("Введите запрос")
        self.search_line.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                border-radius: 15px;
                padding: 10px;
                padding-right: 30px; /* Add padding to the right to make space for the icons */
                font-size: 16px;
                background-color: #f0f0f0;
            }
            QLineEdit::right-inner-addon {
                padding-right: 30px; /* Adjust padding for inner content */
            }
        """)
        self.search_layout.addWidget(self.search_line)

        
        spacer = qtw.QSpacerItem(100, 20, qtw.QSizePolicy.Policy.Expanding, qtw.QSizePolicy.Policy.Minimum)
        self.search_layout.addItem(spacer)




    

        
        
        
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
