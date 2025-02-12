from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE, BIG_FONT_SIZE
from utils import isNumOrDot, isEmpty
from display import Display

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setMinimumSize(75, 75)
        
        
    
class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(rowData):
                if not buttonText:
                    continue
                
                button = Button(buttonText)
   
                if buttonText == '0':
                    self.addWidget(button, rowNumber, 0, 1, 2)
                else:
                    self.addWidget(button, rowNumber, colNumber)

                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextTodisplay,
                    button,
                )
                button.clicked.connect(buttonSlot)

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextTodisplay(self, button):
        button_text = button.text()
        self.display.insert(button_text)
        