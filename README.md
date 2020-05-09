# PySide2

## Instalação

É recomenda a instalação dentro de uma ambiente virtual (pyenv, pipenv, virtualenv, etc)

```bash
pip install PySide2
```

## Como instalar o kirigami2

### Fedora

```bash
sudo dnf install kf5-kirigami2 kf5-kirigami2-devel
```

### Ubuntu

```bash
sudo apt install kirigami2 kirigami2-dev
```

## Tutoriais

- [Instalar o Qt Creator](./docs/install-qt-creator.md).
- [Instalar o Qt Designer](./docs/install-qt-designer.md).

## Código

### Resolução da tela

```python
import sys

app = QApplication(sys.argv)
screen_size = app.primaryScreen().geometry()
screen_size = app.desktop().geometry()
```

Pegar a resolução da tela no QML:

```qml
Screen.desktopAvailableWidth

Screen.desktopAvailableHeight
```

### Estilo

[Utilizando estilos pré definidos](./docs/style.md)

### Python

- [Criando uma janela com QMainWindow](./src/mainwindow/MainWindow.py).
- [Criando uma janela com QWidget](./src/mainwindow/MainWidget.py).

### XML

- [Lendo arquivo XML QMainWindow](./src/mainwindow/xml-qmainwindow).
- [Lendo arquivo XML QWidget](./src/mainwindow/xml-qwidget).

### QML

- [Lendo arquivo QML com QQmlApplicationEngine](./src/mainwindow/qml-engine).
- [Lendo arquivo QML com QQuickView()](./src/mainwindow/qml-qquickview).

### Connect

- [QMainWindow](./src/signals-slots/MainWindow.py).
- [QWidget](./src/signals-slots/MainWidget.py).
- [XML QMainWindow](./src/signals-slots/xml-qmainwindow-connect).
- [XML QWidget](./src/signals-slots/xml-qwidget-connect).
- [QML QQmlApplicationEngine](./src/signals-slots/qml-engine-connect).
- [QML QQuickView](./src/signals-slots/qml-qquickview-connect).

### Slot

- [XML QMainWindow (não está funcionando)](./src/signals-slots/xml-qmainwindow-connect).
- [XML QWidget (não está funcionando)](./src/signals-slots/xml-qwidget-connect).
- [QML QQmlApplicationEngine](./src/signals-slots/qml-engine-slot).

### Barras de menu

- [Barra de menus](src/menus/menubar/MainWindow.py)
- [Barra de status](src/menus/statusbar/MainWindow.py)
- [Barra de ferramentas](src/menus/toolbar/MainWindow.py)

### Layouts

- [QHBoxLayout](./src/layouts/qhboxlayout.py) Layout posiciona os widgets horizontalmente (linha).
- [QVBoxLayout](./src/layouts/qvboxlayout.py) Layout posiciona os widgets verticalmente (coluna).
- [QGridLayout](./src/layouts/qgridlayout.py) Layout posiciona os widgets em celulas (linhas e colunas).
- [QFormLayout](./src/layouts/qformlayout.py) Layout posiciona os widgets como em um formulario (varias linhas 2 colunas).

### Banco de dados

Exemplos de CRUD sem utilizar model:

- [SQLite3](./src/database/db-sqlite/ConnectSQLite.py)
- [PostgreSQL](./src/database/db-postgres/ConnectPostgreSQL.py)