from PyQt6.QtWidgets import QDialog,QVBoxLayout,QFormLayout,QPushButton,QLineEdit,QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from ui.theme import get_stylesheet


class RegisterUser(QDialog):
    def __init__(self,settings,parent=None):
        super().__init__(parent)
        self.settings=settings
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
        self.warning_label.setFixedHeight(30)

        self.registery_layout.addWidget(self.warning_label)
        self.registery_layout.addLayout(self.registery_form)
        self.registery_layout.addWidget(self.submit_btn)
        
        self.setLayout(self.registery_layout)


        self.setWindowIcon(QIcon("logo.ico"))
        self.load_stylesheet()

    
    
    
    
    def load_stylesheet(self):
        qss_string = get_stylesheet(self.settings.value("dark_theme",True,type=bool))
        self.setStyleSheet(qss_string)

    
    
    
    
    def submit(self): #complete later
        pass
