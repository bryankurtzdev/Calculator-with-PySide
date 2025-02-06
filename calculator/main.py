import sys
import qdarkstyle

from main_window import MainWindow
from display import Display
from info import Info
from buttons import Button
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH


def setupTheme(app):
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == '__main__':
    # Cria Aplicacao
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

     # Define o incone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Button
    button = Button()
    window.addToVLayout(button)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()