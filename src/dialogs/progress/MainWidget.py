# -*- coding: utf-8 -*-
"""PySide2 QProgressDialog()."""
import sys

from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QProgressDialog, QPushButton)


class MainWidget(QWidget):
    # Váriável será incrementada e valor é passado para a barra de progresso.
    current_value = 0

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('PySide2 QProgressDialog().')

        # Ícone da janela principal
        icon = QIcon()
        icon.addPixmap(QPixmap('../../../images/icons/icon.png'))
        self.setWindowIcon(icon)

        # Tamanho inicial da janela.
        screen_size = app.desktop().geometry()
        # screen_size = app.primaryScreen().geometry()
        width = screen_size.width()
        height = screen_size.height()
        self.resize(width / 2, height / 2)

        # Tamanho mínimo da janela.
        self.setMinimumSize(width / 2, height / 2)

        # Tamanho maximo da janela.
        self.setMaximumSize(width - 200, height - 200)

        # Widgets.
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.label = QLabel(
            'A janela de processo irá abrir sozinha quando o evento do'
            'timer (QTimer) for iniciado.\n'
            'Ao clicar no botão cancelar o evento é interrompido.\n'
            'Quando o diálogo de progresso atinge o maximo o envento é '
            'interrompido.',
        )
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        button = QPushButton('Abrir diálogo novamente')
        button.clicked.connect(self.start_progress_again)
        vbox.addWidget(button)

        self.progress_dialog = QProgressDialog(
            parent=self,
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
    app = QApplication(sys.argv)
    mainwidget = MainWidget()
    mainwidget.show()
    sys.exit(app.exec_())
