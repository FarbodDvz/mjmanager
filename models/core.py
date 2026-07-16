from PyQt6.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt6.QtGui import QColor
from datetime import datetime
from jdatetime import datetime as jdatetime #use this later

def register_user():
    pass








def add_log(table:QTableWidget,name:str,status):
    table.insertRow(0)

    current_time = datetime.now().strftime("%H:%M:$S")

    table.setItem(0,0,QTableWidgetItem(name))
    table.setItem(0,1,QTableWidgetItem(current_time))

    if status is None:
        table.setItem(0,2,QTableWidgetItem("نامشخص"))
        color = QColor(120,120,120) #gray
    elif status is True:
        table.setItem(0,2,QTableWidgetItem("فعال"))
        color = QColor(0,180,0) #green
    elif status is False:
        table.setItem(0,2,QTableWidgetItem("غیرفعال"))
        color = QColor(200,0,0) #red

    for col in range(3):
        table.item(0,col).setForeground(color)

    if table.rowCount() > 50:
        table.removeRow(table.rowCount() - 1)