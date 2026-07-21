
def get_stylesheet(is_dark_theme): #app theme color: #de8509 Yellow    
    if is_dark_theme:
        return """
        QMainWindow {
        background-color:#000000;
        color: #de8509;
        font-size:16px;
        }

        QWidget {
        background-color:#000000;
        color:#de8509;
        font-size:16px;
        }

        QPushButton {
        background-color:#de8509;
        color:#000000;
        padding:5px 10px;
        border-radius:8px;
        font-size:14px;
        font-weight:bold;
        }
        QPushButton:hover {
        background-color:#1c1c1c;
        color:#de8509;
        }

        QLabel#clocklabel{
        font-weight:bold;
        font-size:18px;   
        }

        """
    



    else:
        return """
        QMainWindow {
        background-color:#f0f0f0;
        color: #1a0f00;
        font-size:16px;
        }

        QWidget {
        background-color:#f0f0f0;
        color:#1a0f00;
        font-size:16px;
        }

        QPushButton {
        background-color:#cfcfcf;
        color:#000000;
        padding:5px 10px;
        border:1px solid black;
        border-radius:8px;
        font-size:14px;
        font-weight:bold;
        }
        QPushButton:hover {
        background-color:#474747;
        color:#de8509;
        }

        QLabel#clocklabel{
        font-weight:bold;
        font-size:18px;   
        }
        """