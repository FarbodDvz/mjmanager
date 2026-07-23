from PyQt6.QtCore import QTime
import jdatetime

def update_clock(clock_label):
    current_time = QTime.currentTime()
    time_text = current_time.toString("HH:mm:ss")
    clock_label.setText(time_text)



def update_date(date_label):
    today = jdatetime.date.today()
    date_info = f"امروز {today.day} {get_jmonth[today.month]} ماه سال {today.year}"
    date_label.setText(date_info)






def get_jmonth(month:int):
    jmonths = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند"
    ]
    return jmonths[month-1]