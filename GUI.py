import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QScrollArea,
    QFrame, QPushButton, QHBoxLayout, QCheckBox, QDialog, QInputDialog
)

from GUI_FUN import functions
from PySide6.QtGui import QIcon
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:

        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        back = QWidget()


        self.setWindowTitle("To-Do")
        self.setWindowIcon(QIcon(resource_path("icon2_task.ico")))
        #self.setWindowIcon(QIcon(r"C:\Windows\System32\shell32.dll"))

        # -----------------------------Background image---------------------------------
        self.setCentralWidget(back)
        back.setObjectName("back")
        paper_path = resource_path("paper-1.jpg")

        back.setStyleSheet(f"""
            #back {{
                background-image: url("{paper_path.replace('\\', '/')}");
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }}
        """)

        # ------------------------------------------------------------------------------

        # ----------------------------------------Shells--------------------------------------------------------
        topLayout = QHBoxLayout()
        layout = QVBoxLayout()
        self.taskInput = QLineEdit()

        self.taskInput.setMaximumWidth(434)
        self.taskInput.setMinimumWidth(36)

        self.add_button = QPushButton("+")
        self.add_button.setMaximumWidth(60)
        self.add_button.setMinimumWidth(30)
        self.add_button.setMaximumHeight(60)

        scroll = QScrollArea()
        scroll.setMaximumSize(500, 700)
        scroll.setMinimumSize(60, 100)
        scroll.setWidgetResizable(True)

        topLayout.addWidget(self.add_button)
        topLayout.addWidget(self.taskInput)
        layout.addLayout(topLayout)
        layout.addWidget(scroll)

        # Set up scroll content and layout
        scrollContent = QWidget()
        self.layoutContent = QVBoxLayout(scrollContent)
        scrollContent.setLayout(self.layoutContent)
        scroll.setWidget(scrollContent)

        layout.setContentsMargins(50, 50, 50, 50)
        layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        back.setLayout(layout)

        # ------------------------------------Functions and Connections---------------------------------------------------------


        self.fun = functions(self.layoutContent, self.taskInput)
        self.fun.load_tasks()

        self.add_button.clicked.connect(self.fun.addtask)
        self.taskInput.returnPressed.connect(self.fun.addtask)

        self.layoutContent.setAlignment(Qt.AlignTop)


#---------------------------------Style------------------------------------
        self.add_button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                color: white;
                background-color: #0b49db;  
                border: none;
                border-radius: 6px;
                padding: 2px;
            }
            QPushButton:hover {
                background-color: #218838;  
            }
            QPushButton:pressed {
                background-color: #b30e0e;  
            }
        """)

        self.taskInput.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                padding: 6px 10px;
                border: 2px solid #0b49db;
                border-radius: 8px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 2px solid #0b49db;
                background-color:white;
            }
        """)

        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                background: transparent;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #999;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background: #666;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)

        scrollContent.setObjectName("taskContainer")
        scrollContent.setStyleSheet("""
            #taskContainer {
                background-color: rgba(255, 255, 255, 0.85);
                border: 2px solid #0b49db;
                border-radius: 8px;
                padding: 10px;
            }
        """)


#---------------------------------Style------------------------------------
app = QApplication(sys.argv)

window = MainWindow()
# window.setFixedSize(500,500)
window.resize(600, 600)
window.show()

app.exec()