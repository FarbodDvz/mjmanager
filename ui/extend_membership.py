from PyQt6.QtWidgets import QDialog,QVBoxLayout,QListWidget,QLineEdit,QHBoxLayout,QLabel
from PyQt6.QtCore import Qt,QTimer
from ui.theme import get_stylesheet



db = {"Alice Smith": {"email": "alice@example.com", "role": "Software Engineer", "office": "NY-101"},
    "Bob Jones": {"email": "bob@example.com", "role": "Project Manager", "office": "LDN-204"},
    "Charlie Brown": {"email": "charlie@example.com", "role": "UI/UX Designer", "office": "SF-302"},
    "Alicia Keys": {"email": "alicia@example.com", "role": "Audio Engineer", "office": "LA-505"}}




class ExtendMembership(QDialog):
    def __init__(self,settings,parent=None):
        super().__init__(parent)
        self.settings = settings

        self.setWindowTitle("تمدید عضویت")
        self.setMinimumWidth(500)



        self.create_widgets()
        self.load_stylesheet()





    def create_widgets(self):
        #LAYOUTS
        main_layout = QVBoxLayout()
        search_bar_layout = QHBoxLayout()
        info_label_layout = QHBoxLayout()



        
        #CREATE WIDGETS
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("نام یا شماره ملی عضو را وارد کنید")
        self.search_bar.setMinimumWidth(250)
        self.search_bar.textChanged.connect(self.on_text_changed)



        self.results_list = QListWidget()
        self.results_list.itemClicked.connect(self.on_item_clicked)

        
        
        self.info_label = QLabel("<i>روی یک کاربر کلیک کنید</i>",self)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)



        self.search_timer = QTimer(self)
        self.search_timer.setSingleShot(True)
        self.search_timer.setInterval(500)
        self.search_timer.timeout.connect(self.perform_search)



        
        
        #ASSIGN TO LAYOUTS
        search_bar_layout.addStretch()
        search_bar_layout.addWidget(self.search_bar)
        search_bar_layout.addStretch()



        info_label_layout.addStretch()
        info_label_layout.addWidget(self.info_label)
        info_label_layout.addStretch()





        main_layout.addLayout(search_bar_layout)
        main_layout.addWidget(self.results_list)
        main_layout.addLayout(info_label_layout)



        self.setLayout(main_layout)





    def load_stylesheet(self):
        qss_string = get_stylesheet(self.settings.value("dark_theme",True,type=bool))
        self.setStyleSheet(qss_string)




    def on_text_changed(self):
        self.search_timer.start()



    def perform_search(self):
        query = self.search_bar.text().strip().lower()
        self.results_list.clear()
        self.info_label.setText("<i>روی یک کاربر کلیک کنید</i>")

        if not query:
            return
        
        for name in db.keys():
            if query in name.lower():
                self.results_list.addItem(name)

        if self.results_list.count() == 0:
            self.results_list.addItem("هیچ عضوی یافت نشد")
            self.results_list.item(0).setFlags(Qt.ItemFlag.NoItemFlags) 




    def on_item_clicked(self,item): #change this later
        name = item.text()
        if name in db:
            info = db[name]
            details = (f"<b>Name:</b> {name}<br>"
                       f"<b>Email:</b> {info['email']}<br>"
                       f"<b>Role:</b> {info['role']}<br>"
                       f"<b>Office:</b> {info['office']}")
            self.info_label.setText(details)