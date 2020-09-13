# -*- coding: utf-8 -*-
"""PySide2 drag and drop.

| Tester 	 | Getter 	   | Setter 	    | MIME Types          |
| ---------- | ----------- | -------------- | ------------------- |
| hasText()  | text() 	   | setText() 	    | text/plain          |
| hasHtml()  | html() 	   | setHtml() 	    | text/html           |
| hasUrls()  | urls() 	   | setUrls() 	    | text/uri-list       |
| hasImage() | imageData() | setImageData() | image/ *            |
| hasColor() | colorData() | setColorData() | application/x-color |

- `QDrag`: Support for MIME-based drag and drop data transfer.
- `QDragEnterEvent`: Event which is sent to a widget when a drag and drop action enters it.
- `QDragLeaveEvent`: Event that is sent to a widget when a drag and drop action leaves it.
- `QDragMoveEvent`: Event which is sent while a drag and drop action is in progress.
- `QDropEvent`: Event which is sent when a drag and drop action is completed.
"""

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap, QPalette
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFrame


class LabelWithDropArea(QLabel):
    def __init__(self):
        super().__init__()
        # Configurando.
        self.setAcceptDrops(True)
        self.setMinimumSize(200, 200)
        self.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        self.setAlignment(Qt.AlignCenter)
        self.setAutoFillBackground(True)

    def dragEnterEvent(self, event):
        """Método é executando quando o arquivo ENTRA na área de drop."""
        print('Drag Enter Event')
        print(f'Event: {event}')

        self.setBackgroundRole(QPalette.Highlight)
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        """Método é executando quando o arquivo entrar na área de drop."""
        print('Drag Move Event')
        print(f'Event: {event}')
        print(f'Posição: {event.pos()}')
        event.accept()

    def dragLeaveEvent(self, event):
        """Método é executando quando o arquivo SAI na área de drop."""
        print('Drag Leave Event')
        print(f'Event: {event}')
        self.setBackgroundRole(QPalette.Base)

    def dropEvent(self, event):
        """Método é executando quando o arquivo é SOLTO na área de drop."""
        print('Drop Event')
        print(event)
        print(event.mimeData())
        print(event.mimeData().text())
        self.setBackgroundRole(QPalette.Base)
        event.acceptProposedAction()


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        # Título da janela.
        self.setWindowTitle('QWidget.')

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

        # Widgets
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        label = QLabel()
        label.setText('Label normal')
        label.setAlignment(Qt.AlignCenter)
        label.setAutoFillBackground(True)
        label.setStyleSheet("QLabel {background-color : red}")
        label.setAcceptDrops(True)
        vbox.addWidget(label)

        label_with_drop_area = LabelWithDropArea()
        label_with_drop_area.setText('Label com drag and drop')
        vbox.addWidget(label_with_drop_area)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainwidget = MainWidget()
    mainwidget.show()
    sys.exit(app.exec_())
