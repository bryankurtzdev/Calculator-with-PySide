import qdarkstyle
from utils import isNumOrDot, isEmpty

qss = """
    QPushButton[cssClass="specialButton"] {
        background-color: #1643FF;
        color: #fff;
    }
    QPushButton[cssClass="specialButton"]:hover {
        background-color: #213291;
    }
    QPushButton[cssClass="specialButton"]:pressed {
        color: #fff;
        background: #2F46CC;
    }
    """

def setupTheme(app):
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

def applySpecialStyle(button, buttonText):
    if not isNumOrDot(buttonText) and not isEmpty(buttonText):
        # Define a propriedade para identificar o botão especial
        button.setProperty('cssClass', 'specialButton')

        # Aplica o estilo personalizado
        button.setStyleSheet(qss)