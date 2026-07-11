from db import models
from ui import ui
import sys
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    models.create_tables()
    app = QApplication(sys.argv)
    window = ui.MainApp()
    window.show()
    sys.exit(app.exec())