from PyQt6.QtCore import QTime

def update_clock(clock_label):
    current_time = QTime.currentTime()
    time_text = current_time.toString("HH:mm:ss")
    clock_label.setText(time_text)