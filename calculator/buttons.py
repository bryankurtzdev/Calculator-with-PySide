from typing import TYPE_CHECKING

from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from styles import applySpecialStyle
from variables import MEDIUM_FONT_SIZE, BIG_FONT_SIZE
from utils import isValidNumber


if TYPE_CHECKING:
    from display import Display
    from info import Info

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(30)
        self.setFont(font)
        font.setBold(True)
        self.setMinimumSize(75, 75)
        
        
    
class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info:'Info', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._equationInitialText = 'Sua conta'
        self._left = None
        self._right = None
        self._operator = None

        self.equation = self._equationInitialText
        self._makeGrid()


    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(rowData):
                if not buttonText:
                    continue
                
                button = Button(buttonText)

                applySpecialStyle(button, buttonText)

                
                if buttonText == '0':
                    self.addWidget(button, rowNumber, 0, 1, 2)
                else:
                    self.addWidget(button, rowNumber, colNumber)

                self._configSpecialButton(button)

                slot = self._makeSlot(
                    self._insertButtonTextTodisplay,
                    button,
                )
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '+-/*':

            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button))

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextTodisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)
        
    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._equationInitialText
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text() # + - * /
        displayText = self.display.text() # devera ser meu numero _left
        self.display.clear() # limpa o display

        # Se a pessoa clicou em um operador e nao tem nada no display
        if not isValidNumber(displayText) and self._left is None:
            print('Nao e nada para passar para a esquerda')
            return
        
        # Se houver algo no numero da esquerda,
        # nao fazemos nada. Aguardaremos o numero da direita
        if self._left is None:
            self._left = float(displayText)

        self._operator = buttonText
        self.equation = f'{self._left} {self._operator} ??'