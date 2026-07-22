import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QDialog,
                             QVBoxLayout, QLineEdit, QListWidget, QLabel)
from PyQt6.QtCore import QTimer, Qt

# A mock database dictionary for demonstration
USER_DATABASE = {
    "Alice Smith": {"email": "alice@example.com", "role": "Software Engineer", "office": "NY-101"},
    "Bob Jones": {"email": "bob@example.com", "role": "Project Manager", "office": "LDN-204"},
    "Charlie Brown": {"email": "charlie@example.com", "role": "UI/UX Designer", "office": "SF-302"},
    "Alicia Keys": {"email": "alicia@example.com", "role": "Audio Engineer", "office": "LA-505"}
}

class SearchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Search Users Database")
        self.resize(400, 300)

        # Main layout for the dialog
        layout = QVBoxLayout(self)

        # 1. The Search Bar (QLineEdit)
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Type a name to search...")
        layout.addWidget(self.search_input)

        # 2. Recommendations List
        self.results_list = QListWidget(self)
        layout.addWidget(self.results_list)

        # 3. User Info Display (QLabel with HTML support)
        self.info_label = QLabel("<i>Select a user to see details.</i>", self)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.info_label.setWordWrap(True)
        layout.addWidget(self.info_label)

        # 4. The Debounce Timer (Wait 500ms before searching)
        self.search_timer = QTimer(self)
        self.search_timer.setSingleShot(True) # Ensure it only fires once per timeout
        self.search_timer.setInterval(500)    # 500 milliseconds

        # 5. Connect Signals and Slots
        self.search_input.textChanged.connect(self.on_text_changed)
        self.search_timer.timeout.connect(self.perform_search)
        self.results_list.itemClicked.connect(self.on_item_clicked)

    def on_text_changed(self, text):
        # Restart the timer every time the user types or deletes a character
        self.search_timer.start()

    def perform_search(self):
        # This function only runs 500ms AFTER the user stops typing
        query = self.search_input.text().strip().lower()
        self.results_list.clear() # Clear the old recommendations
        self.info_label.setText("<i>Select a user to see details.</i>")

        if not query:
            return # Don't search if the box is empty

        # Simulate a database lookup (filtering our dictionary)
        for name in USER_DATABASE.keys():
            if query in name.lower():
                self.results_list.addItem(name)

        # Handle no results
        if self.results_list.count() == 0:
            self.results_list.addItem("No users found.")
            # Disable selection for the "No users found" placeholder
            self.results_list.item(0).setFlags(Qt.ItemFlag.NoItemFlags) 

    def on_item_clicked(self, item):
        # Triggered when a user clicks a name in the QListWidget
        name = item.text()
        if name in USER_DATABASE:
            info = USER_DATABASE[name]
            # Format the output using basic HTML inside the QLabel
            details = (f"<b>Name:</b> {name}<br>"
                       f"<b>Email:</b> {info['email']}<br>"
                       f"<b>Role:</b> {info['role']}<br>"
                       f"<b>Office:</b> {info['office']}")
            self.info_label.setText(details)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My PyQt6 App")
        self.resize(300, 200)

        # Button to open the dialog
        self.button = QPushButton("Open User Search", self)
        self.button.clicked.connect(self.open_search_dialog)
        self.setCentralWidget(self.button)

    def open_search_dialog(self):
        # Instantiate and execute the dialog
        dialog = SearchDialog(self)
        dialog.exec() # Use exec() to make the dialog modal (blocks the main window)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())