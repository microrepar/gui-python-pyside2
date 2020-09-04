# -*- coding: utf-8 -*-
"""QQmlApplicationEngine.

Acessando um arquivo de interface QML `QtQuick.Window` com o
`QQmlApplicationEngine()`.
"""
from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine


class MainWindow(QQmlApplicationEngine):
    def __init__(self):
        super().__init__()

        self.load('./MainWindow.qml')

        if not self.rootObjects():
            sys.exit(-1)


if __name__ == "__main__":
    import sys

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon('../../../../images/icons/icon.png'))
    mainwindow = MainWindow()
    sys.exit(app.exec_())
