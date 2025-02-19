from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from utils import isEmpty

class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Return]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_Return]

        if isEnter or text == '=':
            self.eqPressed.emit()
            return event.ignore()
    
        if isEsc:
            self.delPressed.emit()
            return event.ignore()
        
        if isDelete or text.upper() == 'C':
            self.clearPressed.emit()    
            return event.ignore()
        
        # Nao passar daqui se nao tiver texto
        if isEmpty(text):
            return event.ignore()
        
        print('text:', text)