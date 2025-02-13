import sys

from styles import setupTheme
from main_window import MainWindow
from display import Display
from info import Info
from buttons import Button, ButtonsGrid
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH



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
    info = Info('sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)

    # Button
    button = Button()

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()