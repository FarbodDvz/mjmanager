from PyQt6.QtWidgets import QMainWindow,QWidget,QPushButton,QVBoxLayout,QFormLayout,QLineEdit,QLabel,QDialog
from PyQt6.QtWidgets import QTableWidget,QHeaderView,QHBoxLayout
from PyQt6.QtCore import Qt,QSettings,QTimer
from PyQt6.QtGui import QIcon,QPixmap
from models.core import register_user,add_log
from models.utilities import update_clock
from ui.theme import get_stylesheet

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meysam Jonoub Manager")
        self.setWindowIcon(QIcon("assets/logo.ico"))
        self.resize(800,500)
        self.setMinimumSize(700,400)
        self.center_window()

        self.register_window = None

        self.create_widgets()


        self.settings = QSettings("MJM","App")
        self.load_stylesheet()


    def center_window(self):
        screen = self.screen().availableGeometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) //2,
            (screen.height() - size.height()) //2
        )


    def load_stylesheet(self):
        dark_theme = self.settings.value("dark_theme",True,type=bool)
        qss_string = get_stylesheet(dark_theme)
        self.setStyleSheet(qss_string)
        if dark_theme:
            self.toggle_theme_btn.setText("🌑")
        else:
            self.toggle_theme_btn.setText("☀️")

    
    def update_clock(self):
        update_clock(self.clock_widget)



    def create_widgets(self):
        self.main_widget = QWidget()



        #CREATE LAYOUTS
        main_layout = QVBoxLayout()
        header_hlayout = QHBoxLayout()
        header_vlayout = QVBoxLayout()
        clock_layout = QHBoxLayout()
        buttons_layout = QVBoxLayout()
        new_user_btn_layout = QHBoxLayout()
        extend_membership_btn_layout = QHBoxLayout()
        
        


        #CREATE WIDGETS
        self.logo_label = QLabel()
        pixmap = QPixmap("assets/logo.png")
        self.logo_label.setPixmap(pixmap.scaled(
            100,50,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

        self.logo_label.setMaximumHeight(100)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)





        self.device_status_label = QLabel()
        self.device_status_label.setText("وضعیت دستگاه: نامشخص")





        self.toggle_theme_btn = QPushButton()
        self.toggle_theme_btn.clicked.connect(self.toggle_theme)




        self.clock_widget = QLabel()
        self.clock_widget.setObjectName("clocklabel")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)
        self.update_clock()





        self.new_user_btn = QPushButton("عضویت جدید")
        self.new_user_btn.clicked.connect(self.register_user_window)
        self.new_user_btn.setFixedWidth(150)




        self.extend_membership_btn = QPushButton("تمدید اشتراک عضو")
        self.extend_membership_btn.setFixedWidth(150)
        self.extend_membership_btn.clicked.connect(self.extend_membership_window)





        self.log_table = QTableWidget()
        self.log_table.setColumnCount(3)
        self.log_table.setHorizontalHeaderLabels(["نام","زمان","وضعیت اشتراک"])
        self.log_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.log_table.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
        self.log_table.verticalHeader().setVisible(False)
        header = self.log_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.log_table.setMinimumHeight(300)
        self.log_table.setShowGrid(False)
        self.log_table.setAlternatingRowColors(True)





        #ASSIGN WIDGETS TO LAYOUTS
        header_hlayout.addWidget(self.logo_label)
        header_hlayout.addStretch()
        header_hlayout.addWidget(self.device_status_label)
        header_hlayout.addStretch()
        header_hlayout.addWidget(self.toggle_theme_btn)


        clock_layout.addStretch()
        clock_layout.addWidget(self.clock_widget)
        clock_layout.addStretch()


        header_vlayout.addLayout(header_hlayout)
        header_vlayout.addLayout(clock_layout)


        buttons_layout.addLayout(new_user_btn_layout)
        buttons_layout.addLayout(extend_membership_btn_layout)


        new_user_btn_layout.addStretch()
        new_user_btn_layout.addWidget(self.new_user_btn)
        new_user_btn_layout.addStretch()


        extend_membership_btn_layout.addStretch()
        extend_membership_btn_layout.addWidget(self.extend_membership_btn)
        extend_membership_btn_layout.addStretch()

        
        main_layout.addLayout(header_vlayout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.log_table)

        main_layout.setContentsMargins(15,10,15,10)
        main_layout.setSpacing(10)

        self.main_widget.setLayout(main_layout)
        self.setCentralWidget(self.main_widget)

    
    def toggle_theme(self):
        is_dark_theme = self.settings.value("dark_theme",True,type=bool)
        if is_dark_theme:
            self.settings.setValue("dark_theme",False)
            self.toggle_theme_btn.setText("☀️")
        else:
            self.settings.setValue("dark_theme",True)
            self.toggle_theme_btn.setText("🌑")
        
        self.load_stylesheet()


    def register_user_window(self):
        from ui.register_user_window import RegisterUser
        dialog = RegisterUser(self.settings,parent=self)
        dialog.exec()




    def extend_membership_window(self):
        from ui.extend_membership import ExtendMembership
        dialog = ExtendMembership(self.settings,parent=self)
        dialog.exec()