from db import models
from ui import app
import sys
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    models.create_tables()
    App = QApplication(sys.argv)
    window = app.MainApp()
    window.show()
    sys.exit(App.exec())