# -*- coding: utf-8 -*-
"""PySide2 QInputDialog()."""
import sys

from PySide2.QtCore import Qt, QCoreApplication, QObject, QDir, QTimer
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget, QProgressDialog


class MainWidget(QWidget):
    current_value = 0

    def __init__(self):
        super(MainWidget, self).__init__()
        # Caminho até o arquivo de interface.
        # path = QDir(__file__).currentPath()
        # ui_file = QDir(path).filePath('MainWindow.ui')
        ui_file = QDir(QDir(__file__).currentPath()).filePath('MainWindow.ui')

        self.ui = QUiLoader().load(ui_file, None)

        # Widgets.
        self.label = self.ui.findChild(QObject, 'label')

        button = self.ui.findChild(QObject, 'button')
        button.clicked.connect(self.start_progress_again)

        self.progress_dialog = QProgressDialog(
            parent=self.ui,
            labelText=(
                'Ao clicar em cancelar o timer (QTimer) será parado e a barra '
                'de progresso é reiniciada.'
            ),
            cancelButtonText='Cancelar',
            minimum=0,
            maximum=100,
        )
        self.progress_dialog.setWindowTitle('Titulo da janela de diálogo')
        self.progress_dialog.setModal(True)
        self.progress_dialog.canceled.connect(self.stop_progress)

        self.timer = QTimer()
        self.timer.timeout.connect(self.start_progress)
        self.timer.start(1000)

        self.ui.show()

    def start_progress(self):
        if self.current_value >= self.progress_dialog.maximum():
            self.timer.stop()
            self.progress_dialog.reset()
            self.current_value = 0
        else:
            self.current_value += 10
            self.progress_dialog.setValue(self.current_value)

    def start_progress_again(self):
        self.timer.start(1000)

    def stop_progress(self):
        self.timer.stop()
        self.progress_dialog.reset()
        self.current_value = 0


if __name__ == "__main__":
    # Para evitar o alerta:
    # `Qt WebEngine seems to be initialized from a plugin`.
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    widget = MainWidget()
    sys.exit(app.exec_())
