pyinstaller --noconfirm --log-level=WARN ^
--windowed ^
--name="Exemplo" ^
--add-data="icons\;icons" ^
--add-data="MainWindow.qml;." ^
--icon=icons\icon.ico ^
MainWindow.py