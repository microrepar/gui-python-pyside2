# -*- coding: utf-8 -*-
"""QML QQuickView.

 Essa é uma classe que cria automaticamente uma janela para arquivos
 QML que não possuam uma janela `QtQuick.Window`.
 """
from PySide2.QtCore import QUrl, QSize
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQuick import QQuickView


class MainWindow(QQuickView):

    def __init__(self):
        super().__init__()
        screen_size = app.primaryScreen().geometry()
        width = screen_size.width()
        height = screen_size.height()

        self.setTitle('PySide2 lendo arquivo QML com QQuickView()')
        self.resize(int(width / 2), int(height / 2))
        self.setMinimumSize(QSize(int(width / 3), int(height / 3)))
        self.setResizeMode(QQuickView.SizeRootObjectToView)
        self.setSource(QUrl.fromLocalFile('./MainWindow.qml'))

        if self.status() == QQuickView.Error:
            sys.exit(-1)


if __name__ == '__main__':
    import sys

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('../../assets/icons/icon.png'))
    mainwindow = MainWindow()
    mainwindow.show()
    app.exec_()
