# -*- coding: utf-8 -*-
"""QQmlApplicationEngine e Slot.

Acessando um arquivo de interface QML (`QtQuick.Window`) e utilizando o
`Slot()` para executar um callback.
"""
from PySide2.QtCore import QObject, Slot
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine


class MainWindow(QObject):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.labe1 = self.ui.findChild(QObject, 'label')
        self.text_field = self.ui.findChild(QObject, 'text_field')

    @Slot(str)
    def on_button_clicked(self, text):
        """
        :param text: (str) Valor está sendo enviado do QML para o Python.
        """
        if text:
            self.labe1.setProperty('text', text)
        else:
            self.labe1.setProperty('text', 'Digite algo no campo de texto :)')


if __name__ == "__main__":
    import sys

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('../../../../images/icons/icon.png'))

    engine = QQmlApplicationEngine()
    engine.load('./MainWindow.qml')

    if not engine.rootObjects():
        sys.exit(-1)

    ui = engine.rootObjects()[0]
    mainwindow = MainWindow(ui=ui)

    # Expondo o Python para o QML.
    context = engine.rootContext()

    # python: nome que referência a classe (objeto), esse nome é utilizado no
    # QML para acessar os método que são criados no python.
    # mainwindow: Classe (objeto) com os métodos que serão utilizados no QML.
    context.setContextProperty('python', mainwindow)

    sys.exit(app.exec_())
