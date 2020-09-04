# -*- coding: utf-8 -*-
"""QQuickView e connect.

Acessando um arquivo de interface QML (`QtQuick`) e utilizando o
`connect()` para executar um callback.
"""
from PySide2.QtCore import QObject, QSize, QUrl
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQuick import QQuickView


class MainWindow(QQuickView):
    def __init__(self):
        super().__init__()
        screen_size = app.primaryScreen().geometry()
        width = screen_size.width()
        height = screen_size.height()

        self.setTitle('PySide2 QQuickView e connect')
        self.resize(int(width / 2), int(height / 2))
        self.setMinimumSize(QSize(int(width / 3), int(height / 3)))
        self.setResizeMode(QQuickView.SizeRootObjectToView)
        self.setSource(QUrl.fromLocalFile('./MainWindow.qml'))

        if self.status() == QQuickView.Error:
            sys.exit(-1)

        self.labe1 = self.findChild(QObject, 'label')
        self.text_field = self.findChild(QObject, 'text_field')

        button = self.findChild(QObject, 'button')
        # Conectando o signal a um slot.
        button.clicked.connect(self.on_button_clicked)

        self.show()

    def on_button_clicked(self):
        if self.text_field.property('text'):
            self.labe1.setProperty('text', self.text_field.property('text'))
        else:
            self.labe1.setProperty('text', 'Digite algo no campo de texto :)')


if __name__ == '__main__':
    import sys

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('../../../../images/icons/icon.png'))
    mainwindow = MainWindow()
    sys.exit(app.exec_())
