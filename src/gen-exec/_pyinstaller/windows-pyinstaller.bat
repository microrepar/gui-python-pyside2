pyinstaller --noconfirm --log-level=WARN ^
--windowed ^
--name="Exemplo" ^
--add-data="icons\;icons" ^
--add-data="MainWidget.ui;." ^
--icon=icons\icon.ico ^
MainWidget.py