# -*- coding: utf-8 -*-
"""QQmlApplicationEngine e connect.

Acessando um arquivo de interface QML (`QtQuick.Window`) e utilizando o
`connect()` para executar um callback.
"""
from PySide2.QtCore import QObject
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine


class MainWindow(QObject):

    def __init__(self):
        super().__init__()
        # Variável **DEVE** utilizar `self`!
        self.engine = QQmlApplicationEngine()
        self.engine.load('./MainWindow.qml')
        if not self.engine.rootObjects():
            sys.exit(-1)

        # Variável `window` **DEVE** utilizar `self`!
        # Variável window recebe a janela principal e os widgets.
        self.window = self.engine.rootObjects()[0]

        # Acessado/atribuindo os widgets.
        self.label = self.window.findChild(QObject, 'label')
        self.text_field = self.window.findChild(QObject, 'text_field')

        button = self.window.findChild(QObject, 'button')
        # Conectando o signal a um slot.
        button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        if self.text_field.property('text'):
            self.label.setProperty('text', self.text_field.property('text'))
        else:
            self.label.setProperty('text', 'Digite algo no campo de texto :)')


if __name__ == "__main__":
    import sys

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('../../assets/icons/icon.png'))
    mainwindow = MainWindow()
    sys.exit(app.exec_())
