from PyQt6.QtWidgets import QMainWindow,QWidget,QPushButton,QVBoxLayout,QFormLayout,QLineEdit,QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from models.core import register_user
from theme import get_stylesheet

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meysam Jonoub Manager")
        self.setWindowIcon(QIcon("logo.ico"))

        self.register_window = None

        self.create_widgets()


    def load_stylesheet(self):
        qss_string = get_stylesheet(True) #change the True later
        self.setStyleSheet(qss_string)

    
    
    def create_widgets(self):
        self.main_widget = QWidget()

        vertical_layout = QVBoxLayout()

        self.new_user_btn = QPushButton("عضویت جدید")
        self.new_user_btn.clicked.connect(self.register_user_window)
        
        vertical_layout.addWidget(self.new_user_btn)

        self.main_widget.setLayout(vertical_layout)
        self.setCentralWidget(self.main_widget)


    def register_user_window(self):
        if self.register_window is None:
            self.register_window = RegisterUser()
        
        self.register_window.show()
        self.register_window.raise_()
        self.register_window.activateWindow()






class RegisterUser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ثبت نام عضو جدید")

        self.registery_layout = QVBoxLayout()

        self.registery_form = QFormLayout()
        
        self.submit_btn = QPushButton("ثبت نام")
        self.submit_btn.clicked.connect(self.submit)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("محسن")
        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("یوسفی")
        self.ncode_input = QLineEdit()
        self.ncode_input.setPlaceholderText("۱۲۳۴۵۶۷۸۹۰")
        self.phone_number_input = QLineEdit()
        self.phone_number_input.setPlaceholderText("۰۹۱۲۳۴۵۶۷۸۹")
        #
        # GET FINGERPRINT ID
        #

        self.registery_form.addRow("نام",self.name_input)
        self.registery_form.addRow("نام خانوادگی",self.last_name_input)
        self.registery_form.addRow("کد ملی",self.ncode_input)
        self.registery_form.addRow("شماره موبایل",self.phone_number_input)

        self.warning_label = QLabel("توجه: پر کردن تمام فیلد ها الزامی است")
        self.warning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.warning_label.setFixedHeight(20)

        self.registery_layout.addWidget(self.warning_label)
        self.registery_layout.addLayout(self.registery_form)
        self.registery_layout.addWidget(self.submit_btn)
        
        self.setLayout(self.registery_layout)

    def submit(self): #complete later
        pass